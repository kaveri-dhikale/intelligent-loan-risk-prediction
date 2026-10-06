from pydantic import BaseModel, Field


class LoanApplication(BaseModel):

    Age: int = Field(
        ge=18,
        le=100
    )

    AnnualIncome: float = Field(
        gt=0
    )

    CreditScore: int = Field(
        ge=300,
        le=900
    )

    EmploymentStatus: str

    EducationLevel: str

    LoanAmount: float = Field(
        gt=0
    )

    LoanDuration: int = Field(
        gt=0
    )

    NumberOfDependents: int = Field(
        ge=0
    )

    DebtToIncomeRatio: float = Field(
        ge=0
    )