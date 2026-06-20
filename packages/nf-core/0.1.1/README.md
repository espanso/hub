# nf-core related commands for espanso

## What is nf-core?

[nf-core](https://nf-co.re/) is a community effort for building high-quality, reproducible bioinformatics pipelines with Nextflow.  
It provides:

- Standardized pipeline structure
- Automated linting and CI checks
- Consistent documentation and release practices
- Shared best practices across many pipelines

## What this espanso package is for

This package adds quick text expansions for frequent nf-core comments used in:

- GitHub pull request reviews
- GitHub issues
- Slack support and collaboration

The goal is to make repeated feedback faster, clearer, and more consistent.

## Trigger discovery

Most triggers in this package start with `:nfc-`.

Type `:nfc-` in any text field where Espanso is active (for example GitHub or Slack) to see and use the nf-core shortcuts quickly.

## Available triggers

This package uses grouped triggers with selection popups.
Most groups have one descriptive trigger, with aliases only where helpful.

- `:nfc-lint`
	- Replacement:
		- You can run `nextflow lint -format -sort-declarations -spaces 4 -harshil-alignment` on this file to clean this up nicely.
- `:nfc-modcore`
	- Possible replacements:
		- According to the module specifications we want the module name reflected in the process name.
		- Let the module user decide output naming via `ext-prefix` and use `${prefix}`.
		- Can you please add ontologies to the meta map?
		- Can we put all these inputs into one tuple?
		- If input and output names can overlap, use `task.ext.prefix` to disambiguate (example guard: `if ("${tsv}" == "${prefix}.tsv") ...`).
- `:nfc-versions`
	- Possible replacements:
		- Versions expression snippet:
			- `process.out.findAll { key, val -> key.startsWith('versions') }`
		- Request to migrate versions output to topics.
- `:nfc-snap` (alias: `:nfc-test`)
	- Possible replacements:
		- Use `snapshot(sanitizeOutput(process.out)).match()` for cleaner snapshots.
		- Ask to include more files in snapshots.
		- Use `snapshot(sanitizeOutput(process.out)).match()` for stub assertions.
		- Use `nft-bam` (including `.getReadsMD5()`) for BAM content assertions.
		- Use `nft-vcf` for VCF content assertions.
		- Insert a GitHub ````suggestion```` block with `snapshot(sanitizeOutput(process.out)).match()`.
		- Include `ext.args` in `main.nf.test`.
- `:nfc-docker`
	- Possible replacements:
		- Encourage bringing tools to bioconda so docker/singularity containers can be built automatically.
		- Recommend uploading custom containers to nf-core quay.io and requesting via `#request-core`.
- `:nfc-contrib`
	- Possible replacements:
		- Ask contributor to join the nf-core GitHub organization so CI can run.
		- Recommend one module per PR.
		- Ask to split a large PR into one PR per module/subworkflow.
- `:nfc-thanks`
	- Possible replacements:
		- Thank-you note with mention of added review comments.
		- Thank-you note with guidance to module specs and examples in repository.
- `:nfc-pipeline` (alias: `:nfc-info`)
	- Possible replacements:
		- Request `nextflow.log`, `samplesheet.csv`, and the exact run command.
		- Suggest using a custom configuration file (with docs reference).
- `:prtodo`
	- Replacement:
		- `-commenter:@me -review:changes-requested`
- `:nfc-github` (alias: `:nfc-gh`)
	- Possible replacements:
		- Recommend opening a new PR from the latest module template via `nf-core m create`.
		- Close due to inactivity message with reopen/new PR guidance.

## Typical usage

1. Type a configured trigger in GitHub or Slack.
2. Let espanso expand it into the full comment.
3. Adjust project-specific details before sending.

## Notes

- Keep expansions short, respectful, and actionable.
- Prefer links to nf-core docs when suggesting standards.
- Update triggers regularly as team conventions evolve.