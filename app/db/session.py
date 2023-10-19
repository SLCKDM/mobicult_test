from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

import app.settings as conf


engine = create_async_engine(
    url=conf.DB_URL,
    connect_args={"check_same_thread": False}
)
async_session = async_sessionmaker(
    autocommit=False,
    expire_on_commit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)


async def get_db():
    """ Dependency for getting async db session """
    try:
        session = async_session()
        yield session
    finally:
        await session.aclose()
