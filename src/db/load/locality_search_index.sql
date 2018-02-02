CREATE EXTENSION IF NOT EXISTS unaccent;

CREATE MATERIALIZED VIEW IF NOT EXISTS locality_search_index AS
SELECT id,
       cvegeo,
       location,
       name,
       municipality_name,
       state_name,
       to_tsvector('spanish', unaccent(name)) ||
       to_tsvector('spanish', unaccent(municipality_name)) ||
       to_tsvector('spanish', unaccent(state_name)) as document
FROM map_locality;

CREATE INDEX IF NOT EXISTS idx_fts_locality_search ON locality_search_index USING gin(document);

# refresh index if new locality records are inserted: `REFRESH MATERIALIZED VIEW locality_search_index;`