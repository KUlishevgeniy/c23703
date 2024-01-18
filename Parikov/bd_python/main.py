import sql_interact as sql


if __name__ == '__main__':
    sql.update_rows("name='test_update'",'id_company=1')
    print(*sql.select_rows())