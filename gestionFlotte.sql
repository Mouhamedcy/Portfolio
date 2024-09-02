-- Créer la base de données
CREATE DATABASE GestionFlotte;
USE GestionFlotte;

-- Créer la table des véhicules
CREATE TABLE Vehicles (
    VehicleID INT AUTO_INCREMENT PRIMARY KEY,
    LicensePlate VARCHAR(10) NOT NULL,
    Brand VARCHAR(50) NOT NULL,
    Model VARCHAR(50) NOT NULL,
    Year INT NOT NULL,
    Color VARCHAR(20) NOT NULL,
    VIN VARCHAR(17) NOT NULL UNIQUE
);

-- Créer la table des pilotes
CREATE TABLE Drivers (
    DriverID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    LicenseNumber VARCHAR(15) NOT NULL UNIQUE,
    Phone VARCHAR(15) NOT NULL,
    Address VARCHAR(100) NOT NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(2) NOT NULL,
    ZipCode VARCHAR(10) NOT NULL
);

-- Créer la table des déplacements
CREATE TABLE Trips (
    TripID INT AUTO_INCREMENT PRIMARY KEY,
    VehicleID INT,
    DriverID INT,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    StartLocation VARCHAR(100) NOT NULL,
    EndLocation VARCHAR(100) NOT NULL,
    Distance INT NOT NULL,
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID),
    FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);

-- Créer la table d'entretien
CREATE TABLE Maintenance (
    MaintenanceID INT AUTO_INCREMENT PRIMARY KEY,
    VehicleID INT,
    MaintenanceDate DATE NOT NULL,
    Description VARCHAR(100) NOT NULL,
    Cost DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID)
);

-- Insérer des véhicules
INSERT INTO Vehicles (LicensePlate, Brand, Model, Year, Color, VIN) VALUES
('ABC123', 'Toyota', 'Corolla', 2020, 'Blanc', '1HGCM82633A004352'),
('XYZ789', 'Ford', 'Fusion', 2018, 'Bleu', '2HGCM82633A004353');

-- Insérer des pilotes
INSERT INTO Drivers (FirstName, LastName, LicenseNumber, Phone, Address, City, State, ZipCode) VALUES
('Michael', 'Smith', 'D1234567', '1234567890', '123 Main St', 'Anytown', 'CA', '12345'),
('Sarah', 'Connor', 'D7654321', '0987654321', '456 Elm St', 'Otherville', 'NY', '54321');

-- Insérer des déplacements
INSERT INTO Trips (VehicleID, DriverID, StartDate, EndDate, StartLocation, EndLocation, Distance) VALUES
(1, 1, '2024-07-01', '2024-07-02', 'Los Angeles', 'San Francisco', 380),
(2, 2, '2024-07-03', '2024-07-04', 'New York', 'Washington DC', 225);

-- Insérer des entretiens
INSERT INTO Maintenance (VehicleID, MaintenanceDate, Description, Cost) VALUES
(1, '2024-06-15', 'Vidange d\'huile', 50.00),
(2, '2024-06-20', 'Remplacement des pneus', 300.00);

-- Mettre à jour le coût du deuxième enregistrement de maintenance
UPDATE Maintenance
SET Cost = 350.00
WHERE VehicleID = 2 AND MaintenanceDate = '2024-06-20';

-- Supprimer le premier véhicule du tableau Véhicules
DELETE FROM Vehicles
WHERE LicensePlate = 'ABC123';

-- Insérer un nouvel enregistrement de déplacement
INSERT INTO Trips (VehicleID, DriverID, StartDate, EndDate, StartLocation, EndLocation, Distance) VALUES
(2, 1, '2024-07-05', '2024-07-06', 'Boston', 'Philadelphie', 300);

-- Mettre à jour la couleur du deuxième véhicule
UPDATE Vehicles
SET Color = 'Rouge'
WHERE LicensePlate = 'XYZ789';

-- Insérer un nouvel enregistrement de maintenance
INSERT INTO Maintenance (VehicleID, MaintenanceDate, Description, Cost) VALUES
(1, '2024-07-10', 'Inspection des freins', 100.00);

-- Mettre à jour le numéro de téléphone du premier conducteur
UPDATE Drivers
SET Phone = '2223334444'
WHERE LicenseNumber = 'D1234567';

-- Supprimer le voyage avec TripID = 2
DELETE FROM Trips
WHERE TripID = 2;