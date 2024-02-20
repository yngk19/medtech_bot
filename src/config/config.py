from environs import Env


env = Env()
env.read_env()

BOT_TOKEN: str = env.str("BOT_TOKEN")


PG_HOST: str = env.str("POSTGRES_HOST")
PG_USER: str = env.str("POSTGRES_USER")
PG_PASSWORD: str = env.str("POSTGRES_PASSWORD")
PG_DATABASE: str = env.str("POSTGRES_DB")

USE_CACHE: bool = env.bool("USE_CACHE")

if USE_CACHE:
	REDIS_PORT: str = env.str("REDIS_PORT")
	REDIS_HOST: str = env.str("REDIS_HOST")
	REDIS_USER: str = env.str("REDIS_USER")
	REDIS_PASSWORD: str = env.str("REDIS_PASSWORD")


MEDIA_PATH: str = env.str("MEDIA_PATH")
