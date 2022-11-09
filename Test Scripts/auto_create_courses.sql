SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


USE `spmProj`;

INSERT INTO `courses` (`id`, `name` , `description`, `status`, `type`,   `category`) VALUES
('COR001','Systems Thinking and Design','This foundation module aims to introduce students to the fundamental concepts and underlying principles of systems thinking','Active','Internal','Core'),
('COR002','Lean Six Sigma Green Belt Certification','Apply Lean Six Sigma methodology and statistical tools such as Minitab to be used in process analytics','Active','Internal','Core'),
('SAL001','Risk Management for Smart Business','Apply risk management concepts to digital business','Retired','Internal','Sales'),
('COR004','Service Excellence','The programme provides the learner with the key foundations of what builds customer confidence','Pending','Internal','Core'),
('COR006','Manage Change','Identify risks associated with change and develop risk mitigation plans','Retired','External','Core'),
('FIN003','Business Continuity Planning','Business continuity planning is essential in any business to minimise loss','Retired','External','Finance'),
('MGT001','People Management','Enable learners to manage team performance and development through effective communication','Active','Internal','Management');