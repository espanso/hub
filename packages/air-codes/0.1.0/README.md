# Airports & Airlines Data in Espanso

## Description

The 'air-codes' package is a comprehensive resource for air transportation data, offering convenient access to:

- Properly formatted airport names and locations based on their IATA codes.
- Accurate airline names associated with their respective IATA 2-letter airline identifiers.

## Examples

### Airports Data

Using the `::` trigger followed by an IATA 3-letter airport code and a question mark will reveal detailed information such as the full name, city, and IATA code of the airport. For instance, entering `::MXP?` will provide `Malpensa International Airport, Milan, IT (MXP)`, essentially answering the query "_*What are the details of the airport code MXP?*_".

### Airlines Data

Similarly, using the `::` trigger followed by an IATA 2-letter identifier and a question mark will provide the full name of the airline. For example, entering `::AF?` will display `Air France (AF), FR`, answering the question "_*What are the details of the airline code AF?*_".

## Data Sources

### Airports Data

The airport information is sourced from _*ourairports.com*_, both from their general website ([here](https://ourairports.com/airports.html)) and directly from their data section ([here](https://ourairports.com/data/)). The dataset has been cleaned, enhanced, and curated (to some extend) to focus on 'large_airport' types to ensure a concise package without compromising vital details.

### Airlines Data

The airline data is obtained from _*openflights.org*_ ([here](https://openflights.org/data.php#airline)). The dataset has been refined to include only the airlines with IATA designator codes, while excluding outdated or irrelevant information, ensuring a relevant dataset.

## Relevance

### Why Use This Package?

This package caters to individuals involved in airfreight or logistics, providing a quick and efficient way to access and decode potentially cryptic IATA codes. It serves as a valuable resource for anyone seeking detailed information on airlines and airports within the air transportation industry.

## Disclaimer and Contributions

### Data Accuracy Disclaimer

Considering the volume of data, some information within this dataset was processed automatically. Thus, it's possible that there might be occasional inaccuracies or errors. Your understanding and contribution are appreciated in refining and enhancing this dataset for accuracy.

### Contribution Encouragement

Contributions to improve data accuracy are highly encouraged. If you notice any inaccuracies or errors, please do not hesitate to correct them. Your contributions will help maintain the quality and reliability of the dataset for all users.

## Contact Information

Feel free to reach out for further information or if you're interested in collaborating on projects related to freight or logistics.

You can contact me via:

- [LinkedIn](https://www.linkedin.com/in/cl3mcg/?locale=en_US)
- [Mastodon](https://fosstodon.org/@cl3mcg)
- [Twitter](https://twitter.com/cl3mcg)

I'm open to discussions, collaborations, and suggestions related to air transportation, logistics, or any other relevant projects. Don't hesitate to connect or drop a message via these platforms.

### Other Espanso packages for airport code abbreviations

If you are interested in another Espanso package related to airport code abbreviations and their related cities, check the [`airport-codes` package](https://github.com/gflujan/espanso-airport-codes) from [Gabriel F. Lujan](https://github.com/gflujan).
