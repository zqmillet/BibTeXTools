<img src = "./Logo/Logo.png" width = 250pt />

**BibTeXTools** is designed to process BibTeX file in batches.

## Definition of BibTeX
A typical BibTeX file is shown as follows.

    @LiteratureType{LiteratureHash,
        PropertyName1 = {PropertyValue1},
        PropertyName2 = {PropertyValue2},
        ...
        PropertyNameN = {PropertyValueN}
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
* `-d`, `--delete=PropertyNameList`:<br> delete the property whose name is in `PropertyNameList` of each literature;
* `-l`, `--log=FileName`:<br> save the log into the file `FileName`;
* `-u`, `-geturl`:<br> fetch the Url property of each literature;
* See todo list.

## Examples
Delete all the `ISSN` property of each literature in the `References.bib`.

    BibTeXTools.py -d ISSN References.bib

Delete all the `ISSN` property of each literature, and save as `NoISSN.bib`. The file `References.bib` remains unchanged.

    BibTeXTools.py -d ISSN -o NoISSN.bib References.bib

Delete all the `ISSN`, `Year`, and `Owner` properties of each literature in the `References.bib`.

    BibTeXTools.py -d "ISSN, Year, Owner" References.bib

Delete all the `ISSN`, `Year`, and `Owner` properties of each literature in the `References.bib`, and save the log to the file `References.log`.

    BibTeXTools.py -d "ISSN, Year, Owner" -l References.log References.bib

Update URL property of each literature in the `References.bib`.

    BibTeXTools.py -d Url -u -l References.log References.bib

Then the log is shown as follows.

    2016-05-19 18:00:39: Database References.bib has been loaded.
    2016-05-19 18:00:39: |-The number of literature in References.bib is 4.
    2016-05-19 18:00:39: |-The encoding is utf-8.
    2016-05-19 18:00:39: Delete "Url" properties from References.bib.
    2016-05-19 18:00:39: |-Delete "Url" property from InProceedings -2010-p1-233.
    2016-05-19 18:00:39: |-Delete "Url" property from InProceedings -2008-p609-612.
    2016-05-19 18:00:39: |-Delete "Url" property from Article Zarkovic-2015-p1935-1945.
    2016-05-19 18:00:39: |-Delete "Url" property from Article Acampora-2015-p2397-2411.
    2016-05-19 18:00:39: Fetch "Url" for all literature.
    2016-05-19 18:00:50: |-"Url" property has been added in literature -2010-p1-233.
    2016-05-19 18:00:56: |-"Url" property has been added in literature -2008-p609-612.
    2016-05-19 18:01:01: |-"Url" property has been added in literature Zarkovic-2015-p1935-1945.
    2016-05-19 18:01:09: |-"Url" property has been added in literature Acampora-2015-p2397-2411.
    2016-05-19 18:01:09: The database has been saved as References.bib.

## Built with

* Python 3.5
* PyCharm 2016.1.3

## To Do
* Add swith of case-sensitive.
* Obtain the impact factor of literature according to the property `ISSN`.
* Obtain the full paper of literature accroding to the property `Doi` or `Url`.
* Remove redundant literatures.

## License

This project is licensed under the MIT License. See the [License.md](License.md) file for details.

## Acknowledgments
I would like to thank the anonymous referees for their helpful comments and suggestions.