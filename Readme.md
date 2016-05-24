<img src = "./Logo/Logo.png" width = 250pt />

A Toolkit to Manipulate BibTeX Files.

## Definition of BibTeX
A typical BibTeX file is shown as follows.

    @EntryType{EntryCitationKey,
        TagName1 = {TagContent1},
        TagName2 = {TagContent2},
        ...
        TagNameN = {TagContentN}
    }

## Usage
### Syntax
    BibTeXTools.py [-h] [-d [tag [tag ...]]] [-f [tag [tag ...]]]
                   [--clearempty [tag [tag ...]]]
                   [-r oldtagname newtagname] [-c tagname1 tagname2]
                   [-o file name] [-l] [--logfile file name] [-e encoding]
                   [-v]
                   BibTeXFileName

### Options
* `-h`, `--help`<br> show this help message and exit
* `-d [tag [tag ...]]`, `--delete [tag [tag ...]]`<br> delete tags of all entries in the database.
* `-f [tag [tag ...]]`, `--fetch [tag [tag ...]]`<br> fetch tags of all entries in the database.
* `--clearempty [tag [tag ...]]`<br> clear the empty tags of all entries, if tag name list is empty, all empty tags in database will be deleted.
* `-r oldtagname newtagname`, `--rename oldtagname newtagname`<br> rename tags of all entries from oldtagname to newtagname.
* `-c tagname1 tagname2`, `--copy tagname1 tagname2`<br> copy the tagname1's content content tagname2.
* `-o file name`, `--output file name`<br> set the name of the output file, if this option is not specified, the database will be overwrited.
* `-l`, `--log`<br> save log file.
* `--logfile file name`<br> set the name of the output file, if this option is not specified, the name of log file will be BibTeXFileName.log.
* `-e encoding`, `--encoding encoding`<br> set the encoding of the input file, if this option is not specified, the encoding is utf-8.
* `-v`, `--version`<br> show the version of **BibTeXTools**.

## Examples
Delete the `ISSN` tag of each entry in the `References.bib`.

    BibTeXTools.py References.bib -d ISSN

Delete the `ISSN` tag of each entry, and save the database as file `NoISSN.bib`. The file `References.bib` remains unchanged.

    BibTeXTools.py References.bib -d ISSN -o NoISSN.bib

Delete the `ISSN`, `Year`, and `Owner` tags of each entry in the `References.bib`.

    BibTeXTools.py References.bib -d ISSN Year Owner

Delete the `ISSN`, `Year`, and `Owner` tags of each entry in the `References.bib`, and save the log as the file `References.log`.

    BibTeXTools.py References.bib -d ISSN Year Owner -l

Delete the `Url` tag then fetch `Url` tag of each entry in the `References.bib`.

    BibTeXTools.py References.bib -d Url -f Url -l

Copy the `Url` tag to the `Link` tag of each entry in the `References.bib`, if there is no `Url` tag, the `Link` tag will be created and empty.

    BibTeXTools.py References.bib -c Url Link -l

Rename the `Url` tag to the `Link` tag of each entry in the `References.bib`, if there is no `Url` tag, the corresponding `Link` tag will not be created.

    BibTeXTools.py References.bib --rename Url Link -l

Copy the `Url` tag to the `Link` tag of each entry in the `References.bib`, and clear the empty `Link` tags in the `References.bib`.

    BibTeXTools.py References.bib -c Url Link --clearempty Link -l


## Built with
* Python 3.5
* PyCharm 2016.1.3

## To Do
* Add the function which can fetch the impact factor of entry according to the tag `ISSN`.
* Add the function which can fetch the full paper of entry accroding to the tags `Doi`, `Url` or `Title`.
* Add the function which can remove redundant entries.

## License
This project is licensed under the MIT License. See the [License.md](License.md) file for details.

## Acknowledgments
I would like to thank the anonymous referees for their helpful comments and suggestions.