import pkg_resources
import lxml.etree

schema = lxml.etree.XMLSchema(
    lxml.etree.parse(pkg_resources.resource_stream(
        'koppeltaal_schema', 'xsd/fhir-atom-single.xsd')))


class ValidationError(Exception):

    def __init__(self, message):
        self.message = message


def validate(node):
    schema._clear_error_log()
    # ^^ Is this still necessary
    if not schema.validate(node):
        raise ValidationError(str(schema.error_log))
