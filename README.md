# koppeltaal-schema

XSD schemas for the FHIR messages used by project Koppeltaal. The files are downloaded from [fhir-all-xsd]

NOTE: This package now contain the DSTU2 v1.0.2 version of the schemas. This is not yet in use by the koppeltaal server though.

## How to use?

We use buildout to define dependencies and [pytest] to run the tests:

```sh
$ python2.7 bootstrap.py
$ bin/buildout
$ bin/py.test
```

[pytest]: https://pytest.org
[fhir-all-xsd]: http://hl7.org/fhir/downloads.html
