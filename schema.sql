CREATE TABLE IF NOT EXISTS Contacts
(
    id      INTEGER PRIMARY KEY AUTOINCREMENT,
    name    TEXT,
    email   TEXT,
    phone   TEXT,
    address TEXT,
    alias   TEXT,
    picture BLOB
);

