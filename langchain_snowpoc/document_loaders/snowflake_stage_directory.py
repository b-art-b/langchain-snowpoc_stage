from __future__ import annotations

from typing import List

from langchain_community.document_loaders.base import BaseLoader
from langchain_core.documents import Document
from snowflake.connector.connection import SnowflakeConnection
from snowflake.snowpark.session import Session
from tqdm.auto import tqdm

from langchain_snowpoc.document_loaders.snowflake_stage_file import (
    SnowflakeStageFileLoader,
)


class SnowflakeStageDirectoryLoader(BaseLoader):
    """Load from `Snowflake Stage` directory."""

    def __init__(
        self,
        stage_directory: str,
        *,
        connection: SnowflakeConnection,
    ):
        """Initialize with bucket and key name.

        :param stage_directory: Stage name and path to the directory.
            Example: ``@DB_NAME.SCHEMA_NAME.STAGE_NAME/path/to/dir``

        :param connection: Snowflake connection (SnowflakeConnection).

        """
        self.stage_directory = stage_directory
        self.connection = connection

    def load(self) -> List[Document]:
        """Load documents."""

        docs = []

        session = Session.builder.configs({"connection": self.connection}).create()

        _stage_objects = session.sql(f"LIST {self.stage_directory}").collect()

        for obj in (pbar := tqdm(_stage_objects)):
            file_name = f"@{obj.name}"
            pbar.set_postfix_str(file_name)
            loader = SnowflakeStageFileLoader(
                staged_file_path=file_name, connection=self.connection
            )
            docs.extend(loader.load())
        return docs
