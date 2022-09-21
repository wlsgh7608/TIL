--<ScriptOptions statementTerminator=";"/>

ALTER TABLE `temp`.`departments` DROP PRIMARY KEY;

ALTER TABLE `temp`.`employee_name` DROP PRIMARY KEY;

ALTER TABLE `temp`.`member` DROP PRIMARY KEY;

ALTER TABLE `temp`.`dept_emp` DROP PRIMARY KEY;

ALTER TABLE `temp`.`dept_manager` DROP PRIMARY KEY;

ALTER TABLE `temp`.`employee_docs` DROP PRIMARY KEY;

ALTER TABLE `temp`.`employees` DROP PRIMARY KEY;

ALTER TABLE `temp`.`employees` DROP INDEX `temp`.`ix_hiredate`;

ALTER TABLE `temp`.`departments` DROP INDEX `temp`.`ux_deptname`;

ALTER TABLE `temp`.`dept_emp` DROP INDEX `temp`.`ix_empno_fromdate`;

ALTER TABLE `temp`.`employees` DROP INDEX `temp`.`ix_gender_birthdate`;

ALTER TABLE `temp`.`employee_name` DROP INDEX `temp`.`fx_name`;

ALTER TABLE `temp`.`dept_emp` DROP INDEX `temp`.`ix_fromdate`;

ALTER TABLE `temp`.`employees` DROP INDEX `temp`.`ix_first_name`;

ALTER TABLE `temp`.`dept_emp` DROP INDEX `temp`.`ix_empno_fromdate`;

ALTER TABLE `temp`.`employees` DROP INDEX `temp`.`ix_gender_birthdate`;

DROP TABLE `temp`.`dept_manager`;

DROP TABLE `temp`.`employee_docs`;

DROP TABLE `temp`.`dept_emp`;

DROP TABLE `temp`.`temp_emp`;

DROP TABLE `temp`.`departments`;

DROP TABLE `temp`.`member`;

DROP TABLE `temp`.`employees`;

DROP TABLE `temp`.`employee_name`;

DROP TABLE `temp`.`product`;

CREATE TABLE `temp`.`dept_manager` (
	`dept_no` CHAR(4) NOT NULL,
	`emp_no` INT NOT NULL,
	`from_date` DATE NOT NULL,
	`to_date` DATE NOT NULL,
	PRIMARY KEY (`dept_no`,`emp_no`)
);

CREATE TABLE `temp`.`employee_docs` (
	`doc` null,
	`emp_no` INT NOT NULL,
	PRIMARY KEY (`emp_no`)
);

CREATE TABLE `temp`.`dept_emp` (
	`emp_no` INT NOT NULL,
	`dept_no` CHAR(4) NOT NULL,
	`from_date` DATE NOT NULL,
	`to_date` DATE NOT NULL,
	PRIMARY KEY (`dept_no`,`emp_no`)
);

CREATE TABLE `temp`.`temp_emp` (
	`emp_no` INT NOT NULL,
	`first_name` VARCHAR(14) NOT NULL,
	`last_name` VARCHAR(16) NOT NULL,
	`gender` ENUM NOT NULL
);

CREATE TABLE `temp`.`departments` (
	`dept_no` CHAR(4) NOT NULL,
	`dept_name` VARCHAR(40) NOT NULL,
	`emp_count` INT,
	PRIMARY KEY (`dept_no`)
);

CREATE TABLE `temp`.`member` (
	`no` INT NOT NULL,
	`id` VARCHAR(20) NOT NULL,
	`pw` VARCHAR(20) NOT NULL,
	`name` VARCHAR(50) NOT NULL,
	PRIMARY KEY (`no`)
);

CREATE TABLE `temp`.`employees` (
	`emp_no` INT NOT NULL,
	`birth_date` DATE NOT NULL,
	`first_name` VARCHAR(14) NOT NULL,
	`last_name` VARCHAR(16) NOT NULL,
	`gender` ENUM NOT NULL,
	`hire_date` DATE NOT NULL,
	PRIMARY KEY (`emp_no`)
);

CREATE TABLE `temp`.`employee_name` (
	`emp_no` INT NOT NULL,
	`first_name` VARCHAR(14) NOT NULL,
	`last_name` VARCHAR(16) NOT NULL,
	PRIMARY KEY (`emp_no`)
);

CREATE TABLE `temp`.`product` (
	`productCode` INT,
	`model` VARCHAR(50),
	`price` INT
);

CREATE INDEX `ix_hiredate` ON `temp`.`employees` (`hire_date` ASC);

CREATE INDEX `ux_deptname` ON `temp`.`departments` (`dept_name` ASC);

CREATE INDEX `ix_empno_fromdate` ON `temp`.`dept_emp` (`from_date` ASC);

CREATE INDEX `ix_gender_birthdate` ON `temp`.`employees` (`birth_date` ASC);

CREATE INDEX `fx_name` ON `temp`.`employee_name` (null);

CREATE INDEX `ix_fromdate` ON `temp`.`dept_emp` (`from_date` ASC);

CREATE INDEX `ix_first_name` ON `temp`.`employees` (`first_name` ASC);

CREATE INDEX `ix_empno_fromdate` ON `temp`.`dept_emp` (`emp_no` ASC);

CREATE INDEX `ix_gender_birthdate` ON `temp`.`employees` (`gender` ASC);

