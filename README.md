# koppeltaal-schema

XSD schemas for the FHIR messages used by project Koppeltaal. The files are downloaded from [fhir-all-xsd] with one significant difference:

The "goal" of a CarePlanActivity is a "string" instead of "idref", because the FHIR library used by the Koppeltaal server can't handle this for some reason.

The XSD files are encapsulated in a Python package for easy inclusion in the Python Koppeltaal adapter.

## How to use?

We use buildout to define dependencies and [pytest] to run the tests:

```sh
$ python2.7 bootstrap.py
$ bin/buildout
$ bin/py.test
```

[pytest]: https://pytest.org
[fhir-all-xsd]:http://www.hl7.org/documentcenter/public/standards/FHIR/fhir-all-xsd.zip
