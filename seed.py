import asyncio
from database import async_session_maker
from models import Role, UserRole

async def seed():
    async with async_session_maker() as db:
        for name, desc in [
            ('Admin', 'Full access'),
            ('Analyst', 'Upload and edit'),
            ('Auditor', 'Review'),
            ('Client', 'View')
        ]:
            db.add(Role(name=name, description=desc))
        await db.commit()
        db.add(UserRole(user_id=1, role_id=1))
        await db.commit()
        print('All roles created and Admin assigned to user 1')

asyncio.run(seed())