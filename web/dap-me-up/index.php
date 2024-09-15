<?php
$login_attempted = false;
$login_success = false;
$error_message = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];
    $login_attempted = true;

    if (str_contains($username, "*") || str_contains($password, "*"))
        $error_message = "HACKING ATTEMPT DETECTED!!!";
    else {
        $ldap_host = "ldap://localhost:1389";
        $ldap_dn = "dc=dap-me-up,dc=local";
        $ldap_admin_dn = "cn=admin,dc=dap-me-up,dc=local";
        $ldap_admin_password = "roMZCDMcFfKVhM5nUKyh8VrTf5anpDUt";
        
        $ldap_conn = ldap_connect($ldap_host);
        ldap_set_option($ldap_conn, LDAP_OPT_PROTOCOL_VERSION, 3);
    
        if ($ldap_conn) {
            $ldapbind_admin = ldap_bind($ldap_conn, $ldap_admin_dn, $ldap_admin_password);
            
            if ($ldapbind_admin) {
                $filter = "(&(uid=$username)(userPassword=$password))";
                $result = ldap_search($ldap_conn, $ldap_dn, $filter);
    
                if (!$result)
                    $error_message = "Something went wrong!";
                else {
                    $entries = ldap_get_entries($ldap_conn, $result);
    
                    if ($entries["count"] > 0) {
                        $login_message = "Login success!";
                        $login_success = true;   
                    }
                    else
                        $error_message = "Invalid username or password!";
                }
            }
    
            ldap_close($ldap_conn);
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dap Me Up</title>
    <link href='http://fonts.googleapis.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
    <style>
        body {
            font-family: 'Open Sans';
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }

        .login-box {
            width: 510px;
            height: 280px;
            text-align: center;
            box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
            border-radius: 10px;

            form {
                display: flex;
                flex-direction: column;
                padding-bottom: 10px;

                input {
                    box-sizing: border-box;
                    margin-left: auto;
                    margin-right: auto;
                    margin-bottom: 10px;
                    width: 80%;
                    height: 40px;
                    border: none;
                    border-radius: 4px;
                    background-color: #efefef;
                    padding: 10px;
                    font-size: 14px;
                }

                input[type="submit"] {
                    cursor: pointer;
                }
            }

            div {
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
        }
    </style>
</head>
<body>
    <div class="login-box">
        <?php
        if ($login_success) {
        ?>
            <div>
                <h1 style="margin: 0">🤝👊</h1>
                <h2>Here's the flag!</h2>
                <span>gigem{c0n6r475_y0u_f0und_ld4p_1nj3c710n_w17h0u7_*}</span>
            </div>
        <?php
        }
        else {
        ?>
            <h2>LOGIN</h2>
            <form action="index.php" method="POST">
                <input name="username" placeholder="Username" required/>
                <input type="password" placeholder="Password" name="password" required/>
                <input type="submit" value="Submit">
            </form>
            <span>
                <?php 
                if ($login_attempted)
                    echo $error_message;
                else
                    echo "Please login to dap me up.";
                ?>
            </span>
        <?php
        }
        ?>
    </div>
</body>
</html>
