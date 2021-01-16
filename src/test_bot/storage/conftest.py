import boto3
import localstack_client.session
import pytest


@pytest.fixture(autouse=True)
def boto3_localstack_patch(monkeypatch):
    session_ls = localstack_client.session.Session(localstack_host="localstack")
    monkeypatch.setattr(boto3, "client", session_ls.client)
    monkeypatch.setattr(boto3, "resource", session_ls.resource)
