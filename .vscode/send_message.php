<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Include PHPMailer files (make sure you have them in the correct location)
require 'PHPMailer/Exception.php';
require 'PHPMailer/PHPMailer.php';
require 'PHPMailer/SMTP.php';

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and retrieve form data
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    // Create a new PHPMailer instance
    $mail = new PHPMailer(true);

    try {
        // Set up SMTP server
        $mail->isSMTP();
        $mail->Host = 'smtp.gmail.com'; // Gmail SMTP server
        $mail->SMTPAuth = true;
        $mail->Username = 'sk2579784@gmail.com'; // Your Gmail address
        $mail->Password = 'your-email-password'; // Your Gmail password or App Password
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;
        $mail->Port = 587;

        // Set sender and recipient
        $mail->setFrom($email, $name);
        $mail->addAddress('sk2579784@gmail.com'); // Your email address to receive the messages

        // Set email content
        $mail->Subject = "New Contact Form Submission from $name";
        $mail->Body = "You have received a new message from your website contact form.\n\n" .
                      "Name: $name\n" .
                      "Email: $email\n" .
                      "Message:\n$message\n";

        // Send the email
        $mail->send();
        echo "<script>alert('Message sent successfully!'); window.location.href = '/';</script>";
    } catch (Exception $e) {
        echo "<script>alert('Message failed to send: {$mail->ErrorInfo}'); window.history.back();</script>";
    }
}
?>
