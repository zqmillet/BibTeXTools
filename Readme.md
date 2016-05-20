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
    BibTeXTools.py [options] BibTeXFileName.bib
or

    BibTeXTools.py BibTeXFileName.bib [options]

### Options
* `-v`, `--version`:<br> show the version of **BibTeXTools**;
* `-h`, `--help`:<br> show the usage of **BibTeXTools**;
* `-o`, `--output=FileName`:<br> set the name of output file;
* `-d`, `--delete=TagNameList`:<br> delete the tag whose name is in `TagNameList` of each entry;
* `-l`, `--log=LogFileName`:<br> save the log as the file `LogFileName`;
* `-u`, `-fetchurl`:<br> fetch the Url tag of each entry;
* See todo list.

## Examples
Delete the `ISSN` tag of each entry in the `References.bib`.

    BibTeXTools.py -d ISSN References.bib

Delete the `ISSN` tag of each entry, and save the database as file `NoISSN.bib`. The file `References.bib` remains unchanged.

    BibTeXTools.py -d ISSN -o NoISSN.bib References.bib

Delete the `ISSN`, `Year`, and `Owner` tags of each entry in the `References.bib`.

    BibTeXTools.py -d "ISSN, Year, Owner" References.bib

Delete the `ISSN`, `Year`, and `Owner` tags of each entry in the `References.bib`, and save the log as the file `References.log`.

    BibTeXTools.py -d "ISSN, Year, Owner" -l References.log References.bib

Fetch `Url` tag of each entry in the `References.bib`.

    BibTeXTools.py -d Url -u -l References.log References.bib

Then the log is shown as follows.

    2016-05-20 16:45:55: Database References.bib has been loaded.
    2016-05-20 16:45:55: |-The encoding is utf-8.
    2016-05-20 16:45:55: |-The number of entries in References.bib is 13.
    2016-05-20 16:45:55:   |-The number of TechReport(s) is 1
    2016-05-20 16:45:55:   |-The number of Article(s) is 7
    2016-05-20 16:45:55:   |-The number of InProceedings(s) is 5
    2016-05-20 16:45:55: Delete "Url" properties from References.bib.
    2016-05-20 16:45:55: |-Delete "Url" tag from InProceedings Chen-2010-p393-400.
    2016-05-20 16:45:55: |-Delete "Url" tag from Article Dove-2009-p7-10.
    2016-05-20 16:45:55: |-Delete "Url" tag from Article Hu-2016-p449-475.
    2016-05-20 16:45:55: |-Delete "Url" tag from Article Luthar-2000-p543-562.
    2016-05-20 16:45:55: |-Delete "Url" tag from Article Qi-2011-p770-781.
    2016-05-20 16:45:55: |-Delete "Url" tag from InProceedings Rieger-2009-p632-636.
    2016-05-20 16:45:55: |-Delete "Url" tag from InProceedings Rieger-2012-p143-148.
    2016-05-20 16:45:55: |-Delete "Url" tag from InProceedings Sousa-2007-p373-380.
    2016-05-20 16:45:55: |-Delete "Url" tag from Article Sridhar-2012-p210-224.
    2016-05-20 16:45:55: |-Delete "Url" tag from InProceedings Wei-2010-p15-22.
    2016-05-20 16:45:55: |-Delete "Url" tag from Article Yu-2016-p1058-1070.
    2016-05-20 16:45:55: |-Delete "Url" tag from Article Zhou-2012-p1439-1453.
    2016-05-20 16:45:55: Fetch "Url" for all entries.
    2016-05-20 16:45:55: |-There is no "Doi" tag in TechReport Alliance-2013-p-. Try Title tag.
    2016-05-20 16:46:05: |-"Url" tag has been added in InProceedings Chen-2010-p393-400.
    2016-05-20 16:46:13: |-"Url" tag has been added in Article Dove-2009-p7-10.
    2016-05-20 16:46:20: |-"Url" tag has been added in Article Hu-2016-p449-475.
    2016-05-20 16:46:28: |-"Url" tag has been added in Article Luthar-2000-p543-562.
    2016-05-20 16:46:36: |-"Url" tag has been added in Article Qi-2011-p770-781.
    2016-05-20 16:46:43: |-"Url" tag has been added in InProceedings Rieger-2009-p632-636.
    2016-05-20 16:46:50: |-"Url" tag has been added in InProceedings Rieger-2012-p143-148.
    2016-05-20 16:46:58: |-"Url" tag has been added in InProceedings Sousa-2007-p373-380.
    2016-05-20 16:47:05: |-"Url" tag has been added in Article Sridhar-2012-p210-224.
    2016-05-20 16:47:13: |-"Url" tag has been added in InProceedings Wei-2010-p15-22.
    2016-05-20 16:47:20: |-"Url" tag has been added in Article Yu-2016-p1058-1070.
    2016-05-20 16:47:30: |-"Url" tag has been added in Article Zhou-2012-p1439-1453.
    2016-05-20 16:47:30: The database has been saved as References.bib.

## Built with
* Python 3.5
* PyCharm 2016.1.3

## To Do
* Add the function which can fetch the impact factor of entry according to the tag `ISSN`.
* Add the function which can fetch the full paper of entry accroding to the tags `Doi`, `Url` or `Title`.
* Remove redundant entries.

## License
This project is licensed under the MIT License. See the [License.md](License.md) file for details.

## Acknowledgments
I would like to thank the anonymous referees for their helpful comments and suggestions.