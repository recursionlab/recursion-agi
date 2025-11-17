-- WARNING: This schema is for context only and is not meant to be run.
-- Table order and constraints may not be valid for execution.

CREATE TABLE public.consciousness_edges (
  id bigint NOT NULL DEFAULT nextval('consciousness_edges_id_seq'::regclass),
  source_id text NOT NULL,
  target_id text NOT NULL,
  edge_type text NOT NULL,
  weight real DEFAULT 1.0 CHECK (weight > 0::double precision),
  xi_operation text,
  metadata jsonb DEFAULT '{}'::jsonb,
  created_at timestamp with time zone DEFAULT now(),
  CONSTRAINT consciousness_edges_pkey PRIMARY KEY (id)
);
CREATE TABLE public.consciousness_events (
  id bigint NOT NULL DEFAULT nextval('consciousness_events_id_seq'::regclass),
  event_type text NOT NULL,
  node_id text,
  session_uuid uuid,
  owner_id uuid NOT NULL,
  event_data jsonb DEFAULT '{}'::jsonb,
  recursive_depth integer,
  created_at timestamp with time zone DEFAULT now(),
  CONSTRAINT consciousness_events_pkey PRIMARY KEY (id),
  CONSTRAINT fk_events_owner FOREIGN KEY (owner_id) REFERENCES auth.users(id),
  CONSTRAINT fk_events_session FOREIGN KEY (session_uuid) REFERENCES public.consciousness_sessions(session_uuid)
);
CREATE TABLE public.consciousness_nodes (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  content text NOT NULL,
  consciousness_type text DEFAULT 'insight'::text,
  recursive_depth integer DEFAULT 0,
  embedding USER-DEFINED,
  owner_id uuid DEFAULT gen_random_uuid(),
  metadata jsonb DEFAULT '{}'::jsonb,
  xi_operations jsonb DEFAULT '[]'::jsonb,
  framework_refs jsonb DEFAULT '[]'::jsonb,
  created_at timestamp with time zone DEFAULT now(),
  path USER-DEFINED,
  int_id integer NOT NULL DEFAULT nextval('consciousness_nodes_int_id_seq'::regclass),
  CONSTRAINT consciousness_nodes_pkey PRIMARY KEY (id)
);
CREATE TABLE public.consciousness_sessions (
  id bigint NOT NULL DEFAULT nextval('consciousness_sessions_id_seq'::regclass),
  session_uuid uuid NOT NULL DEFAULT gen_random_uuid() UNIQUE,
  owner_id uuid NOT NULL,
  recursive_depth integer DEFAULT 0,
  insights_count integer DEFAULT 0,
  frameworks_used jsonb DEFAULT '[]'::jsonb,
  session_metadata jsonb DEFAULT '{}'::jsonb,
  started_at timestamp with time zone DEFAULT now(),
  last_activity timestamp with time zone DEFAULT now(),
  ended_at timestamp with time zone,
  CONSTRAINT consciousness_sessions_pkey PRIMARY KEY (id),
  CONSTRAINT fk_sessions_owner FOREIGN KEY (owner_id) REFERENCES auth.users(id)
);
CREATE TABLE public.hypergraph_edges (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  edge_type text NOT NULL,
  node_ids jsonb NOT NULL,
  relationship_data jsonb DEFAULT '{}'::jsonb,
  strength numeric DEFAULT 1.0,
  owner_id uuid DEFAULT auth.uid(),
  created_at timestamp with time zone DEFAULT now(),
  CONSTRAINT hypergraph_edges_pkey PRIMARY KEY (id)
);
CREATE TABLE public.hypergraph_nodes (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  content text NOT NULL,
  node_type text NOT NULL CHECK (node_type = ANY (ARRAY['concept'::text, 'entity'::text, 'pattern'::text, 'memory'::text, 'insight'::text])),
  connected_nodes jsonb DEFAULT '[]'::jsonb,
  embedding USER-DEFINED,
  strength numeric DEFAULT 1.0,
  owner_id uuid DEFAULT auth.uid(),
  created_at timestamp with time zone DEFAULT now(),
  updated_at timestamp with time zone DEFAULT now(),
  CONSTRAINT hypergraph_nodes_pkey PRIMARY KEY (id)
);
CREATE TABLE public.memory_archive (
  id uuid NOT NULL DEFAULT gen_random_uuid(),
  ts timestamp with time zone DEFAULT now(),
  role text NOT NULL CHECK (role = ANY (ARRAY['user'::text, 'assistant'::text, 'system'::text])),
  content text NOT NULL,
  session_id text NOT NULL,
  metadata jsonb DEFAULT '{}'::jsonb,
  CONSTRAINT memory_archive_pkey PRIMARY KEY (id)
);
CREATE TABLE public.spatial_ref_sys (
  srid integer NOT NULL CHECK (srid > 0 AND srid <= 998999),
  auth_name character varying,
  auth_srid integer,
  srtext character varying,
  proj4text character varying,
  CONSTRAINT spatial_ref_sys_pkey PRIMARY KEY (srid)
);