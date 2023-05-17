-- Create the candidate table
CREATE TABLE candidate (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(50),
  role VARCHAR(50),
  education VARCHAR(50)
);

-- Insert some sample data into the candidate table
INSERT INTO candidate (id, name, role, education)
VALUES (1, 'Srinivas', 'Developer', 'Computer Science'),
       (2, 'Sridevi', 'Designer', 'Graphic Design'),
       (3, 'Sunaina', 'Developer', 'Computer Science'),
       (4, 'Pranaya', 'Tester', 'Electronics'),
       (5, 'Tarun Raj', 'DBA', 'Computer Science'),
       (6, 'Tarun Ghanta', 'Developer', 'System Design'),
       (7, 'Nagasai', 'QA', 'Computer Science');

-- Create the certificate table
CREATE TABLE certificate (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(50),
  fee DECIMAL(8, 2)
);

-- Insert some sample data into the certificate table
INSERT INTO certificate (id, name, fee)
VALUES (1, 'Oracle Certified Professional Java SE 11 Developer', 245),
       (2, 'AWS Certified Solutions Architect - Associate', 150),
       (3, 'AWS Certified Cloud Practitioner', 150),
       (4, 'Service Now Certification', 200),
       (5, 'Oracle Java Certification', 175);

-- Create the candidate_certificates table
CREATE TABLE candidate_certificates (
  candidate_id INT NOT NULL,
  certificate_id INT NOT NULL,
  on_date DATE,
  PRIMARY KEY (candidate_id, certificate_id),
  FOREIGN KEY (candidate_id) REFERENCES candidate(id),
  FOREIGN KEY (certificate_id) REFERENCES certificate(id)
);

-- Insert some sample data into the candidate_certificates table
INSERT INTO candidate_certificates (candidate_id, certificate_id, on_date)
VALUES (1, 1, '2022-01-01'),
       (1, 2, '2022-02-01'),
       (2, 2, '2022-03-12'),
       (2, 2, '2022-05-01'),
       (3, 1, '2022-04-01'),
       (3, 2, '2022-03-21'),
       (4, 5, '2022-03-02');

