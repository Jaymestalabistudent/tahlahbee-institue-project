                        List of relations
 Schema |     Name     | Type  |              Owner               
--------+--------------+-------+----------------------------------
 public | contribution | table | tahlahbee_institute_postgre_user
 public | post         | table | tahlahbee_institute_postgre_user
 public | story        | table | tahlahbee_institute_postgre_user
 public | user         | table | tahlahbee_institute_postgre_user
(4 rows)



                                         Table "public.post"
   Column    |            Type             | Collation | Nullable |             Default              
-------------+-----------------------------+-----------+----------+----------------------------------
 id          | integer                     |           | not null | nextval('post_id_seq'::regclass)
 title       | character varying(100)      |           | not null | 
 date_posted | timestamp without time zone |           | not null | 
 content     | text                        |           | not null | 
 user_id     | integer                     |           | not null | 
Indexes:
    "post_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "post_user_id_fkey" FOREIGN KEY (user_id) REFERENCES "user"(id)





                                       Table "public.contribution"
   Column    |           Type           | Collation | Nullable |                 Default                  
-------------+--------------------------+-----------+----------+------------------------------------------
 id          | integer                  |           | not null | nextval('contribution_id_seq'::regclass)
 content     | text                     |           | not null | 
 date_posted | timestamp with time zone |           | not null | 
 story_id    | integer                  |           | not null | 
 user_id     | integer                  |           | not null | 
Indexes:
    "contribution_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "contribution_story_id_fkey" FOREIGN KEY (story_id) REFERENCES story(id)
    "contribution_user_id_fkey" FOREIGN KEY (user_id) REFERENCES "user"(id)






                                      Table "public.user"
   Column   |          Type          | Collation | Nullable |             Default              
------------+------------------------+-----------+----------+----------------------------------
 id         | integer                |           | not null | nextval('user_id_seq'::regclass)
 username   | character varying(20)  |           | not null | 
 email      | character varying(120) |           | not null | 
 image_file | character varying(20)  |           | not null | 
 password   | character varying(60)  |           | not null | 
Indexes:
    "user_pkey" PRIMARY KEY, btree (id)
    "user_email_key" UNIQUE CONSTRAINT, btree (email)
    "user_username_key" UNIQUE CONSTRAINT, btree (username)
Referenced by:
    TABLE "contribution" CONSTRAINT "contribution_user_id_fkey" FOREIGN KEY (user_id) REFERENCES "user"(id)
    TABLE "post" CONSTRAINT "post_user_id_fkey" FOREIGN KEY (user_id) REFERENCES "user"(id)





                                      Table "public.story"
   Column    |          Type          | Collation | Nullable |              Default              
-------------+------------------------+-----------+----------+-----------------------------------
 id          | integer                |           | not null | nextval('story_id_seq'::regclass)
 title       | character varying(100) |           | not null | 
 description | text                   |           | not null | 
Indexes:
    "story_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "contribution" CONSTRAINT "contribution_story_id_fkey" FOREIGN KEY (story_id) REFERENCES story(id)

