# Good Morning
*A simple python-powered match that creates personalized greetings that look like they were manually typed.*

## Summary
Each time the **:morning** match is called the script will generate a list of greetings for each name in the names.txt file. Names that include the tag character from the script (:) will be prioritized in the order they appear. Other names will be added to the list in a semi-random order.

A random greeting will then be appended to the output depending on the day of the week.

A good morning GIF file can also be optionally downloaded to the resources folder, which can then be output with the **:img-morning** match.

## Matches
* **:morning** - Generates a semi-random list of good morning greetings.

* **:img-morning** - Outputs a random morning themed GIF **that is optionally downloaded when the :morning is called**.

## Configuration
The script and configuration files are located in the resources folder:
* **names.txt** - Contains the list of names that will be included in the final message.

* **config.json** - Contains script configuration options:
    * **downloadImage** - Determines whether or not to download an image from the configured repository. Default value is false.
    * **repo** - Repository to download image from in the format of {owner}/{repositor}
    * **path** - Image folder path within specified repository (e.g files/images)
    * **branch** - Branch of specified repository
    * **personalGreetings** - Greetings that will be used on each line (e.g. Hello, Good morning, etc.)
    * **weekdayGreetings** - Greetings that will be used on each weekday unless otherwise specified.
    * **mondayGreetings** - Greetings that will be used on Mondays.
    * **fridayGreetings** - Greetings that will be used on Frindays.

Greetings for each category can be added to the arrays their respective fields.

For security reasons, downloading images is disabled by default. In order to enable this functionality, the following must be configured:
* downloadImage must be set to **true**.
* repo must be configured with the owner and repository portions of the **GitHub repository url from which you would like to download images**.
* If the images reside in a subdirectory of the repository, the path must be specified with the path option.
* If the images reside in a specific branch of the repository, the branch must be specified by name via the branch option.

*For convenience, an example configuration with image downloading enabled has been provided via the example-config.json file.*

## Example
Good morning, Tom!<br>
Good morning, Katelyn!<br>
Good morning, Fred!<br>
Good morning, Anna!<br>
Good morning, Andrew!<br>
Good morning, Mary!<br>
Good morning, Bob!<br>
Good morning, Ted!<br>

It's going to be a great day!