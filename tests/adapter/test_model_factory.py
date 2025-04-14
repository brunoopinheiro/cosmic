import pytest

from cosmic.adapter.xml.model_factory import ModelFactory, UppaalAdapter


def test_xml_model_factory():
    adapter = ModelFactory.xml_model_factory("uppaal")
    assert isinstance(adapter, UppaalAdapter)


def test_xml_model_factory_not_supported():
    with pytest.raises(NotImplementedError):
        ModelFactory.xml_model_factory("astah")


def test_xml_model_factory_invalid_dialect():
    with pytest.raises(ValueError):
        ModelFactory.xml_model_factory("invalid")
