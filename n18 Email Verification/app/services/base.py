from uuid import UUID

from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession

class BaseService:
    def __init__(self, model: SQLModel, session: AsyncSession):
        self.model = model       
        self.session = session

    async def _get(self, id: UUID):
        return await self.session.get(self.model, id)

    async def _add(self, entity: SQLModel):
        self.session.add(entity)           
        await self.session.commit()        
        await self.session.refresh(entity) 
        return entity

    async def _update(self,entity: SQLModel):
        return await self._add(entity)

    async def _delete(self,id:UUID):

        product = await self._get(id)
        if product is None:
            return False
        await self.session.delete(product)
        await self.session.commit()
        return True

