-- Create the candidate table
CREATE TABLE candidate (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(50),
  role VARCHAR(50),
  education VARCHAR(50)
);

-- Insert some sample data into the candidate table
INSERT INTO candidate (id, name, role, education)
VALUES (1, 'John Smith', 'Developer', 'Computer Science'),
       (2, 'Jane Doe', 'Designer', 'Graphic Design');

-- Create the certificate table
CREATE TABLE certificate (
  id INT NOT NULL PRIMARY KEY,
  name VARCHAR(50),
  fee DECIMAL(8, 2)
);

-- Insert some sample data into the certificate table
INSERT INTO certificate (id, name, fee)
VALUES (1, 'Oracle Certified Professional Java SE 11 Developer', 245),
       (2, 'AWS Certified Solutions Architect - Associate', 150);

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
       (2, 2, '2022-03-01');

