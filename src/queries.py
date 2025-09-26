#%%
create_schema = "CREATE SCHEMA IF NOT EXISTS `bluepeak_technologies` DEFAULT CHARACTER SET utf8 ;"

use_schema = "USE `bluepeak_technologies`;"

create_table_employee = """CREATE TABLE IF NOT EXISTS `bluepeak_technologies`.`employee` (
  `employeenumber` INT NOT NULL,
  `attrition` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`employeenumber`),
  UNIQUE INDEX `employeenumber_UNIQUE` (`employeenumber` ASC) VISIBLE
) ENGINE = InnoDB;"""

create_table_employee_demographics = """CREATE TABLE IF NOT EXISTS `bluepeak_technologies`.`employee_demographics` (
  `employeenumber` INT NOT NULL,
  `age` INT NULL,
  `gender` VARCHAR(45) NULL,
  `marital_status` VARCHAR(45) NULL,
  `date_birth` DATETIME NULL,
  `generation` VARCHAR(45) NULL,
  `education` VARCHAR(45) NULL,
  `educationfield` VARCHAR(45) NULL,
  `distance_from_home` VARCHAR(45) NULL,
  `employee_employeenumber` INT NOT NULL,
  UNIQUE INDEX `employeenumber_UNIQUE` (`employeenumber` ASC) VISIBLE,
  INDEX `fk_employee_demographics_employee_idx` (`employee_employeenumber` ASC) VISIBLE,
  CONSTRAINT `fk_employee_demographics_employee`
    FOREIGN KEY (`employee_employeenumber`)
    REFERENCES `bluepeak_technologies`.`employee` (`employeenumber`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;"""

create_table_employee_professional = """CREATE TABLE IF NOT EXISTS `bluepeak_technologies`.`employee_professional` (
  `employeenumber` INT NOT NULL,
  `job_role` VARCHAR(100) NULL,
  `departament` VARCHAR(100) NULL,
  `years_at_company` INT NULL,
  `num_companies_worked` INT NULL,
  `over_time` VARCHAR(45) NULL,
  `training_times_last_year` INT NULL,
  `years_in_current_role` INT NULL,
  `job_level` INT NULL,
  `business_travel` VARCHAR(45) NULL,
  `standard_hours` VARCHAR(45) NULL,
  `remote_work` VARCHAR(45) NULL,
  `employee_employeenumber` INT NOT NULL,
  UNIQUE INDEX `employeenumber_UNIQUE` (`employeenumber` ASC) VISIBLE,
  INDEX `fk_employee_professional_employee1_idx` (`employee_employeenumber` ASC) VISIBLE,
  CONSTRAINT `fk_employee_professional_employee1`
    FOREIGN KEY (`employee_employeenumber`)
    REFERENCES `bluepeak_technologies`.`employee` (`employeenumber`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;"""

create_table_employee_financial = """CREATE TABLE IF NOT EXISTS `bluepeak_technologies`.`employee_financial` (
  `employeenumber` INT NOT NULL,
  `monthly_income` DECIMAL(10,2) NULL,
  `monthly_rate` DECIMAL(10,2) NULL,
  `salary` DECIMAL(10,2) NULL,
  `stock_option_level` INT NULL,
  `daily_rate` DECIMAL(8,2) NULL,
  `percent_salary_hike` DECIMAL(5,2) NULL,
  `employee_employeenumber` INT NOT NULL,
  UNIQUE INDEX `employeenumber_UNIQUE` (`employeenumber` ASC) VISIBLE,
  INDEX `fk_employee_financial_employee1_idx` (`employee_employeenumber` ASC) VISIBLE,
  CONSTRAINT `fk_employee_financial_employee1`
    FOREIGN KEY (`employee_employeenumber`)
    REFERENCES `bluepeak_technologies`.`employee` (`employeenumber`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;"""

create_table_employee_satisfaction = """CREATE TABLE IF NOT EXISTS `bluepeak_technologies`.`employee_satisfaction` (
  `employeenumber` INT NOT NULL,
  `job_satisfaction` INT NULL,
  `performance_rating` INT NULL,
  `relationship_satisfaction` INT NULL,
  `work_life_balance` INT NULL,
  `environment_satisfaction` INT NULL,
  `job_involvement` INT NULL,
  `employee_employeenumber` INT NOT NULL,
  UNIQUE INDEX `employeenumber_UNIQUE` (`employeenumber` ASC) VISIBLE,
  INDEX `fk_employee_satisfaction_employee1_idx` (`employee_employeenumber` ASC) VISIBLE,
  CONSTRAINT `fk_employee_satisfaction_employee1`
    FOREIGN KEY (`employee_employeenumber`)
    REFERENCES `bluepeak_technologies`.`employee` (`employeenumber`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;"""
