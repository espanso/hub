# Copyright (c) Asyntai. Licensed under the MIT license.
#
# Asyntai AI Assistant for Espanso, Windows side.
#
# Espanso runs this script through the shell extension (see package.yml) and
# types whatever it prints. macOS and Linux run asyntai.py, which does the
# same work.
#
#   ask    question from the :ask form (ESPANSO_FORM1_QUESTION)
#   clip   question from the clipboard (ESPANSO_CLIP)
#   key    save the API key from the :asyntaikey form (ESPANSO_FORM1_KEY)
#
# The script only talks to asyntai.com, only sends the API key in the
# Authorization header, and only writes one file: the saved API key.
# It needs nothing but Windows PowerShell 5.1, which every Windows 10 and 11
# has.

param([string]$Mode)

$ErrorActionPreference = 'Stop'

$LiveBase = 'https://asyntai.com'
$UserAgent = 'AsyntaiEspanso/0.1'
$TimeoutMs = 90000
# The other Asyntai launchers mark their own questions the same way, so the
# owner's test questions are easy to tell apart from visitor chats.
$AskMarker = 'espanso_ask_'

$NoKey = 'Asyntai: add your API key first. Type :asyntaikey in an empty text field.'
$BadKey = 'Asyntai: this API key no longer works. Type :asyntaikey and paste a new key.'

function New-AsyntaiError([string]$Message, [int]$Status = 0) {
    $e = New-Object System.Exception $Message
    $e.Data['asyntai'] = $true
    $e.Data['status'] = $Status
    return $e
}

function Get-KeyPath {
    $root = $env:APPDATA
    if (-not $root) { $root = $env:USERPROFILE }
    return [IO.Path]::Combine($root, 'asyntai', 'espanso-api-key')
}

function Read-Key {
    if ($env:ASYNTAI_API_KEY -and $env:ASYNTAI_API_KEY.Trim()) { return $env:ASYNTAI_API_KEY.Trim() }
    $path = Get-KeyPath
    if (Test-Path -LiteralPath $path) {
        return ([IO.File]::ReadAllText($path, [Text.Encoding]::UTF8)).Trim()
    }
    return ''
}

function Save-Key([string]$Key) {
    $path = Get-KeyPath
    [void][IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($path))
    [IO.File]::WriteAllText($path, $Key, (New-Object Text.UTF8Encoding $false))
}

function Get-BaseUrl {
    # A local Asyntai server can be used for development, nothing else, so
    # the key can never be sent to a third-party host.
    $base = "$env:ASYNTAI_BASE_URL".Trim().TrimEnd('/')
    if ($base) {
        try {
            $uri = New-Object Uri $base
            if ($uri.Host -eq '127.0.0.1' -or $uri.Host -eq 'localhost') { return $base }
        } catch { }
    }
    return $LiveBase
}

function Invoke-Asyntai([string]$Method, [string]$Path, [string]$Key, $Body) {
    [Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12
    $request = [Net.HttpWebRequest]::Create((Get-BaseUrl) + $Path)
    $request.Method = $Method
    # Never follow a redirect: it could send the question or the API key to
    # another host. A 3xx answer becomes an error instead.
    $request.AllowAutoRedirect = $false
    $request.Timeout = $TimeoutMs
    $request.ReadWriteTimeout = $TimeoutMs
    $request.UserAgent = $UserAgent
    $request.Accept = 'application/json'
    $request.Headers['Authorization'] = 'Bearer ' + $Key

    $response = $null
    try {
        if ($null -ne $Body) {
            $bytes = [Text.Encoding]::UTF8.GetBytes(($Body | ConvertTo-Json -Compress))
            $request.ContentType = 'application/json; charset=utf-8'
            $request.ContentLength = $bytes.Length
            $stream = $request.GetRequestStream()
            $stream.Write($bytes, 0, $bytes.Length)
            $stream.Close()
        }
        $response = $request.GetResponse()
    } catch {
        $inner = $_.Exception
        while ($inner -and -not ($inner -is [Net.WebException])) { $inner = $inner.InnerException }
        if ($inner -and $inner.Response) { $response = $inner.Response }
    }
    if ($null -eq $response) {
        throw (New-AsyntaiError 'Asyntai: no answer from asyntai.com. Check your internet connection and try again.')
    }

    $status = [int]$response.StatusCode
    $reader = New-Object IO.StreamReader($response.GetResponseStream(), [Text.Encoding]::UTF8)
    $text = $reader.ReadToEnd()
    $reader.Close()
    $response.Close()

    $root = $null
    if ($text.Trim()) {
        try { $root = $text | ConvertFrom-Json } catch { $root = $null }
    } else {
        $root = New-Object PSObject
    }
    $message = ''
    if ($root -and ($root.error -is [string])) { $message = $root.error }

    if ($status -eq 401) { throw (New-AsyntaiError $BadKey $status) }
    if ($status -eq 403) {
        if (-not $message) { $message = 'the Asyntai API needs the Starter plan or higher.' }
        throw (New-AsyntaiError ('Asyntai: ' + $message) $status)
    }
    if ($status -eq 429) {
        if (-not $message) { $message = 'your chatbot reached its message limit.' }
        throw (New-AsyntaiError ('Asyntai: ' + $message) $status)
    }
    if ($status -lt 200 -or $status -ge 300 -or $null -eq $root -or $root.success -eq $false) {
        if (-not $message) { $message = "the server answered with status $status." }
        throw (New-AsyntaiError ('Asyntai: ' + $message) $status)
    }
    return $root
}

function ConvertTo-Plain([string]$Text) {
    # Make a chat answer fit a plain text field: links as "text (url)", no bold.
    $Text = [regex]::Replace($Text, '\[([^\]]*)\]\((\S+?)\)', {
        param($m)
        $label = $m.Groups[1].Value.Trim()
        $url = $m.Groups[2].Value.Trim()
        if (-not $label -or $label -eq $url -or $url.StartsWith('mailto:') -or $url.StartsWith('tel:')) {
            if ($label) { return $label } else { return $url }
        }
        return "$label ($url)"
    })
    $Text = [regex]::Replace($Text, '(?s)\*\*(.+?)\*\*', '$1')
    $Text = [regex]::Replace($Text, '(?s)__(.+?)__', '$1')
    $Text = [regex]::Replace($Text, '(?m)^#{1,6}[ \t]+', '')
    $Text = $Text -replace "`r`n", "`n"
    $Text = [regex]::Replace($Text, '\n{3,}', "`n`n")
    return $Text.Trim()
}

function Invoke-Ask([string]$Question) {
    $Question = "$Question".Trim()
    if (-not $Question) { return 'Asyntai: the question is empty. Type :ask and write a question.' }
    $key = Read-Key
    if (-not $key) { return $NoKey }
    $session = $AskMarker + [DateTimeOffset]::UtcNow.ToUnixTimeMilliseconds() + '_' + [guid]::NewGuid().ToString('N').Substring(0, 6)
    $root = Invoke-Asyntai 'POST' '/api/v1/chat/' $key @{ message = $Question; session_id = $session }
    $answer = ''
    if ($root.response -is [string]) { $answer = ConvertTo-Plain $root.response }
    if (-not $answer) { return 'Asyntai: your chatbot gave an empty answer.' }
    return $answer
}

function Set-AsyntaiKey([string]$Key) {
    $Key = "$Key".Trim()
    if (-not $Key) { return 'Asyntai: the API key is empty. Type :asyntaikey and paste your key.' }
    try {
        $root = Invoke-Asyntai 'GET' '/api/v1/websites/' $Key $null
    } catch {
        if ($_.Exception.Data['status'] -eq 401) {
            return 'Asyntai: this is not a valid API key. In Asyntai, open Settings, then API, and copy the key again.'
        }
        throw
    }
    # Save only a key that Asyntai accepts.
    Save-Key $Key
    $sites = @($root.websites | Where-Object { $_ -ne $null })
    $primary = @($sites | Where-Object { $_.is_primary -eq $true }) + $sites | Select-Object -First 1
    if ($primary -and ($primary.domain -is [string]) -and $primary.domain) {
        return "Asyntai API key saved. Your chatbot for $($primary.domain) is ready: type :ask to ask it."
    }
    return 'Asyntai API key saved. Type :ask to ask your chatbot.'
}

try {
    switch ($Mode) {
        'ask' { $out = Invoke-Ask $env:ESPANSO_FORM1_QUESTION }
        'clip' { $out = Invoke-Ask $env:ESPANSO_CLIP }
        'key' { $out = Set-AsyntaiKey $env:ESPANSO_FORM1_KEY }
        default { $out = 'Asyntai: unknown command.' }
    }
} catch {
    if ($_.Exception.Data['asyntai']) { $out = $_.Exception.Message }
    else { $out = 'Asyntai: something went wrong. Please try again.' }
}

# Espanso reads stdout as UTF-8. Write the bytes directly, so the console
# code page cannot change the text.
$bytes = [Text.Encoding]::UTF8.GetBytes($out)
$stdout = [Console]::OpenStandardOutput()
$stdout.Write($bytes, 0, $bytes.Length)
$stdout.Flush()
