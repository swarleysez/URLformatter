# URLformatter.py
Python script to format Sublist3r output into a list usable by Eyewitness or httpscreenshot

## Purpose
URLformatter was created to take output from Sublist3r and format it into URLs per subdomain per port that can be used with [EyeWitness](https://github.com/ChrisTruncer/EyeWitness) (`-f <URL_file.txt>`) and/or [httpscreenshot](https://github.com/breenmachine/httpscreenshot) (`-l <URL_file.txt`).

## Requirements
* This was created for the intention of being used with my forked Sublist3r project: [https://github.com/swarleysez/Sublist3r](https://github.com/swarleysez/Sublist3r)
  * Unfortunately, as of right now only my forked Sublist3r project will create a commna-delimited file that can be used with URLformatter.py, Excel, LibreOffice Calc, etc.
* Sublist3r has to be ran with at least 1 port supplied and querying IP addresses:
  * `python sublist3t.py -d example.com -i -p 80,443 -o <URL_file.txt>`
    * `-d` : Target domain
    * `-i` : Switch to query for IP addresses of discovered subdomains
    * `-p` : User-supplied ports
    * `-o` : File for output

Note: The script only supports parsing 2 ports. This will be expanded to any number of ports in the future.

## Usage
### Example
`python URLformatter.py <input_file.txt.> <output_file.txt>`

## ToDo
* [ ] Expand for any number of ports
* [ ] Clean up statements for consolidation
* [ ] Parse output from other tools (Recon-NG, discover.sh)
