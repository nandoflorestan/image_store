"""Strategies for storing file payloads."""

from abc import ABCMeta, abstractmethod


class BasePayloadStorage(metaclass=ABCMeta):
    """Abstract base class ― formal interface for payload storage backends."""

    def __init__(self, orchestrator):
        """Just store the orchestrator instance."""
        self.orchestrator = orchestrator

    @abstractmethod
    def put(self, namespace, metadata, bytes_io):
        """Store a file (``bytes_io``) inside ``namespace``."""
        raise NotImplementedError()

    @abstractmethod
    def get_reader(self, namespace, metadata):
        """Return an open "file" object from which the payload can be read.

        Otherwise, raise KeyError.
        """
        raise NotImplementedError()

    @abstractmethod
    def get_url(self, namespace, metadata):
        """Return an URL for a certain stored file."""
        raise NotImplementedError()

    @abstractmethod
    def delete(self, namespace, metadatas):
        """Delete many files within a namespace."""
        raise NotImplementedError()

    '''
    @abstractmethod
    def gen_keys(self, namespace):
        """Generate the existing keys in a namespace."""
        raise NotImplementedError()

    @abstractmethod
    def delete_namespace(self, namespace):
        """Delete all files in ``namespace``."""
        raise NotImplementedError()
    '''
