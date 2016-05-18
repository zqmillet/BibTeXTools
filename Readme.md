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
* See todo list.

## Examples
Delete all the `ISSN` property of each literature in the `References.bib`.

    BibTeXTools.py -d ISSN References.bib

Delete all the `ISSN` property of each literature, and save as `NoISSN.bib`. The file `References.bib` remains unchanged.

    BibTeXTools.py -d ISSN -o NoISSN.bib References.bib

Delete all the `ISSN`, `Year`, and `Owner` properties of each literature in the `References.bib`.

    BibTeXTools.py -d "ISSN, Year, Owner" References.bib

## Built with

* Python 3.5
* PyCharm 2016.1.3

## To Do
* Obtain the impact factor of literature according to the property `ISSN`.
* Obtain the full paper of literature accroding to the property `Doi` or `Url`.
* Remove redundant literatures.

## License

This project is licensed under the MIT License. See the [License.md](License.md) file for details.

## Acknowledgments
I would like to thank the anonymous referees for their helpful comments and suggestions.