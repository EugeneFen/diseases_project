init_db = '''
    DROP TABLE IF EXISTS diseases;
    CREATE TABLE diseases (
        id_diseases INTEGER PRIMARY KEY AUTOINCREMENT, 
        name_diseases TEXT NOT NULL UNIQUE
    );

    DROP TABLE IF EXISTS signs;
    CREATE TABLE signs (
        id_signs INTEGER PRIMARY KEY AUTOINCREMENT,
        name_signs TEXT NOT NULL UNIQUE
    );

    DROP TABLE IF EXISTS normal_values;
    CREATE TABLE normal_values (
        id_normal_values INTEGER PRIMARY KEY AUTOINCREMENT,
        id_signs INTEGER NOT NULL,
        value_nv TEXT NOT NULL,
        FOREIGN KEY (id_signs)
            REFERENCES signs (id_signs)
              ON DELETE CASCADE
              ON UPDATE NO ACTION
    );

    DROP TABLE IF EXISTS possible_values;
    CREATE TABLE possible_values (
        id_possible_values INTEGER PRIMARY KEY AUTOINCREMENT,
        id_signs INTEGER NOT NULL,
        value_pv TEXT NOT NULL,
        FOREIGN KEY (id_signs)
            REFERENCES signs (id_signs)
              ON DELETE CASCADE
              ON UPDATE NO ACTION
    );

    DROP TABLE IF EXISTS clinical_picture;
    CREATE TABLE clinical_picture (
        id_clinical_picture INTEGER PRIMARY KEY AUTOINCREMENT,
        id_diseases INTEGER NOT NULL,
        id_signs INTEGER NOT NULL,
        FOREIGN KEY (id_signs)
            REFERENCES signs (id_signs)
              ON DELETE CASCADE
              ON UPDATE NO ACTION,
        FOREIGN KEY (id_diseases)
           REFERENCES diseases (id_diseases)
              ON DELETE CASCADE
              ON UPDATE NO ACTION
    );

    DROP TABLE IF EXISTS characteristics_values;
    CREATE TABLE characteristics_values (
        id_characteristics_values INTEGER PRIMARY KEY AUTOINCREMENT,
        id_diseases INTEGER NOT NULL,
        id_signs INTEGER NOT NULL,
        value_cv TEXT NOT NULL,
        FOREIGN KEY (id_signs)
            REFERENCES signs (id_signs)
              ON DELETE CASCADE
              ON UPDATE NO ACTION,
        FOREIGN KEY (id_diseases)
           REFERENCES diseases (id_diseases)
              ON DELETE CASCADE
              ON UPDATE NO ACTION
    );
'''