import uuid

from infra.postgres.postgres import Base
from sqlalchemy import Column, Float, String
from sqlalchemy.dialects.postgresql import UUID


class Organization(Base):
    __tablename__ = 'organization'
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        unique=True,
    )
    name = Column(
        String,
        nullable=False,
    )


class Build(Base):
    __tablename__ = 'build'
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        unique=True,
    )
    adress = Column(
        String,
        nullable=False
    )
    coordinates = Column(
        Float,
        nullable=False,
    )


class Activity(Base):
    __tablename__ = 'activity'
    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        unique=True,
    )
    name = Column(
        String,
        nullable=False,
    )
