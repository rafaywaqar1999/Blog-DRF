from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL('CREATE OR REPLACE FUNCTION get_all_blog_posts() RETURNS SETOF blogpost_blogpost AS $$ BEGIN RETURN QUERY SELECT * FROM blogpost_blogpost; END; $$ LANGUAGE plpgsql;'),

        migrations.RunSQL('CREATE OR REPLACE FUNCTION update_last_blog() RETURNS TRIGGER AS $$ BEGIN UPDATE "users_customuser" SET blog_post = NEW.id WHERE id = NEW.author_id; RETURN NEW; END; $$ LANGUAGE plpgsql;'),

        migrations.RunSQL('CREATE TRIGGER blog_post_created AFTER INSERT ON blogpost_blogpost FOR EACH ROW EXECUTE FUNCTION update_last_blog();'),
    ]
