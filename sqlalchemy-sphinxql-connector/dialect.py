""" Dialect implementaiton for SphinxQL based on MySQLdb-Python protocol"""

from sqlalchemy.engine import default

__all__ = ("SphinxDialect")



class SphinxDialect(default.DefaultDialect):

    name = "sphinx"

    # TODO HACK : Prevent SQLalchemy to send the request
    # 'SELECT 'X' as some_label;' as it is not supported by Sphinx
    description_encoding = None

    def _get_server_version_info(self, connection):
        return (0, '')
    
    def _get_default_schema_name(self, connection):
        pass
    
    def _detect_charset(self, connection):
        pass    
 
    def _detect_casing(self, connection):
        pass
    
    def _detect_collations(self, connection):
        pass
    
    def _detect_ansiquotes(self, connection):
        self._server_ansiquotes = False        

    def _detect_sql_mode(self, connection):
        self._sql_mode = ""

    def get_isolation_level(self, connection):
        pass        
    
    def _check_unicode_returns(self, connection):
        return True

    def do_rollback(self, connection):
        pass

    def do_commit(self, connection):
        pass

    def do_begin(self, connection):
        pass
