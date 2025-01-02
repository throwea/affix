### This file contains methods needed for using the LLAMA Index txt2SQL 
from llama_index.core.query_engine import NLSQLTableQueryEngine
from llama_index.core.utilities.sql_wrapper import SQLDatabase
import openai
from llama_index.llms.openai import OpenAI
import os
from llama_index.core.indices.struct_store.sql_query import (
    SQLTableRetrieverQueryEngine,
)
from llama_index.core.objects import (
    SQLTableNodeMapping,
    ObjectIndex,
    SQLTableSchema,
)
from llama_index.core import VectorStoreIndex
openai.api_key = os.environ["OPENAI_KEY"]

#PERF: In the future, if we have more companies we can cache these indexes in memory

#WARN: This will only work for one table
def execute_pipeline_single_table(user_msg: str, tables: list[str], sql_database: SQLDatabase) -> str: 
    """
    This method runs the text to SQL pipeline and provides 
    an answer to a users question about their own data
    """
    llm = OpenAI(temperature=0.1, model="gpt-3.5-turbo") #TODO: is it possible to manually call the LLM through our own method so we can track token usage
    query_engine = NLSQLTableQueryEngine(
        sql_database=sql_database, tables=tables, llm=llm
    )
    response = query_engine.query(user_msg)
    return response

def execute_pipeline_many_table(user_msg: str, tables: list[str], sql_database: SQLDatabase) -> str: 
    """
    This method runs the text to SQL pipeline and provides 
    an answer to a users question about their own data.
    However, this method will collect data across multiple tables
    """
    # set Logging to DEBUG for more detailed outputs
    table_node_mapping = SQLTableNodeMapping(sql_database)
    table_schema_objs = __collect_tables() #TODO: this method needs to collect all of the data related to a specific company
    #TODO: make sure each table has an explanation as well. Refer to block comment in part 2 of the poc notebook
    obj_index = ObjectIndex.from_objects(
        table_schema_objs,
        table_node_mapping,
        VectorStoreIndex,
    )
    query_engine = SQLTableRetrieverQueryEngine(
        sql_database, obj_index.as_retriever(similarity_top_k=1)
    )
    response = query_engine.query(user_msg)
    return response

def __collect_tables() -> list[SQLTableSchema]:
    """
    This method is used to collect all of the table schemas
    so we can create an index to be used when we perform a query across tables
    """
    #INFO: Since I'm storing multiple disparate tables across one database (for now) this method will need to ensure
    #that only the tables under the user's company is being included when the index is created. I'm thinking that it might be better
    #to do this operation somewhere else since it requires accessing the DB. I want to decouple DB from LLM operations
    return []
