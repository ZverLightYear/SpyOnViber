from __future__ import annotations
from abc import ABC

import pytest


class TestV2ATranslationSuite(ABC):
    @pytest.mark.skip
    def test_model_to(self, adapter, expect_model):
        assert adapter.model_to() == expect_model

    @pytest.mark.skip
    def test_model_from(self, adapter, expect_model):
        assert adapter.model_from() == expect_model

    @pytest.mark.skip
    def test_models(self, adapter, expect_models):
        assert adapter.models() == expect_models

