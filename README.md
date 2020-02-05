# eMERGE FHIR Specification

This is a ReadTheDocs project that is the source of the eMERGE FHIR specification.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See build the documentation locally. All changes committed to
this project will automatically trigger the build of the readthedocs.io project that publishes
the http://emerge-fhir-spec.readthedocs.io/en/latest/.

### Prerequisites

python 3.7.4

```
Install Python3... after install
>pip3 --version
pip 19.1.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)
```

### Installing

A step by step series of examples that tell you how to get the project building

Install the sphinx project requirements

```
cd docs
-- in docs folder
pip3 install -r requirements.txt
```

Build the documentation from the docs folder

```
make html
```

View the local documentation build

```
open bulid/html/index.html
```

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/emerge-ehri/fhir-specification/tags).

## Authors

* **Mullai Murugan** - *Initial work* - [BCM-HGSC](https://www.hgsc.bcm.edu/)
* **Larry Babb** - *Initial work* - [Broad Institute](https://www.broadinstitute.org/)

**TBD** See also the list of [contributors](https://github.com/emerge-ehri/fhir-specification/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* HL7 CG Working Group - FHIR CG IG
* etc
