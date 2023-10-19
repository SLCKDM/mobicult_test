from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

engine = create_async_engine(url='sqlite+aiosqlite://', connect_args={"check_same_thread": False})
async_session = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


async def get_db():
    """ Dependency for getting async db session """
    try:
        session = async_session()
        yield session
    finally:
        await session.aclose()
