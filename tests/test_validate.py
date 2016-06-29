import py.path
import lxml.etree
import pytest
from koppeltaal_schema.validate import validate, ValidationError


here = py.path.local(__file__)


def test_validate_xsd():
    stanza = lxml.etree.fromstring('<frop/>')
    with pytest.raises(ValidationError) as cm:
        validate(stanza)
    assert cm.value.message == (
        '''<string>:1:0:ERROR:SCHEMASV:SCHEMAV_CVC_ELT_1: '''
        '''Element 'frop': No matching global declaration available '''
        '''for the validation root.''')


def test_create_or_update_careplan():
    xml = here.dirpath() / 'examples/CreateOrUpdateCarePlan.xml'
    stanza = lxml.etree.parse(str(xml))
    assert validate(stanza) is None


@pytest.mark.xfail(reason='waiting for Bart M to provide more information')
def test_create_or_update_careplan_activity_result():
    xml = here.dirpath() / 'examples/CreateOrUpdateCarePlanActivityResult.xml'
    stanza = lxml.etree.parse(str(xml))
    assert validate(stanza) is None


def test_create_or_update_user_message():
    xml = here.dirpath() / 'examples/CreateOrUpdateUserMessage.xml'
    stanza = lxml.etree.parse(str(xml))
    assert validate(stanza) is None


@pytest.mark.xfail(reason='waiting for Bart M to provide more information')
def test_update_user_care_plan_activity_status():
    xml = here.dirpath() / 'examples/UpdateCarePlanActivityStatus.xml'
    stanza = lxml.etree.parse(str(xml))
    assert validate(stanza) is None
