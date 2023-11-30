from src.model.declarative_base import Session, engine, Base
from src.model.employer import Employer
from src.model.work import Work
from src.model.voucher import Voucher
from src.model.employee import Employee
from src.model.company_data import CompanyData
from src.model.discount import Discount
from src.model.remuneration import Remuneration

if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    session = Session()



    session.commit()
    session.close()