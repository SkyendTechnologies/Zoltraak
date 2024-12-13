from sqlalchemy import Column, Integer, String, Float, DateTime


class ModelA:
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)

    def __repr__(self):
        return f"ModelA(id={self.id}, name={self.name}, value={self.value}, timestamp={self.timestamp})"