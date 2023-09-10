<?php
// (A) RODO KOA KONFIGU
require dirname(__DIR__) . DIRECTORY_SEPARATOR . "lib" . DIRECTORY_SEPARATOR . "CORE-Config.php";

// (B) PHP MODIFICATIONS
if (!defined("PATH_CHATBOT")) {
  try {
    // (B1) BACKUP CONFIG FILE
    copy(PATH_LIB . "CORE-Config.php", PATH_LIB . "CORE-Config.old");
  
    // (B2) ADD URL & PATH
    $url = parse_url(HOST_BASE, PHP_URL_SCHEME) . "://" . HOST_NAME . ":8008";
    $add = <<<EOD
    // ADDED BY INSTALLER - AI CHATBOT
    define("PATH_CHATBOT", PATH_BASE . "chatbot" . DIRECTORY_SEPARATOR);
    define("HOST_CHATBOT", "$url");
    EOD;
    $fh = fopen(PATH_LIB . "CORE-Config.php", "a");
    fwrite($fh, "\r\n\r\n$add");
    fclose($fh);
  } catch (Exception $ex) {
    exit("Unable to update CORE-Config.php - " . $ex->getMessage());
  }

  try {
    // (B3) BACKUP TEMPLATE TOP
    copy(PATH_PAGES . "TEMPLATE-top.php", PATH_PAGES . "TEMPLATE-top.old");

    // (B4) ADD NEW "AI" MENU ITEM
    $template = file(PATH_PAGES . "TEMPLATE-top.php");
    foreach ($template as $j=>$line) {
      if (strpos($line, "</i> Reports") !== false) {
        array_splice($template, $j+2, 0, [
          "\r\n", "<!-- (AI ASSISTANT) ADDED BY INSTALLER -->\r\n",
          '<a class="nav-link ms-1" href="<?=HOST_BASE?>ai">' . "\r\n",
          '<i class="text-secondary ico-sm icon-stats-dots"></i> AI Assistant' . "\r\n",
          '</a>' . "\r\n"
        ]);
        break;
      }
    }

    // (B5) SAVE
    file_put_contents(PATH_PAGES . "TEMPLATE-top.php", implode("", $template));
    unset($template);
  } catch (Exception $ex) {
    exit("Unable to update TEMPLATE-top.php - " . $ex->getMessage());
  }
  
  // (B6) NEW CHATBOT PATH
  define("PATH_CHATBOT", PATH_BASE . "chatbot" . DIRECTORY_SEPARATOR);
}

// (C) BACKUP CHATBOT/A_SETTINGS.PY
if (!copy(PATH_CHATBOT . "a_settings.py", PATH_CHATBOT . "a_settings.old")) {
  exit("Failed to backup settings file - " . PATH_CHATBOT . "a_settings.old");
}

// (D) COPY SETTINGS FROM CORE-CONFIG.PHP TO A_SETTINGS.PY
$replace = [
  "http_allow" => "[\"http://".HOST_NAME."\", \"https://".HOST_NAME."\"]",
  "http_host" => "\"".HOST_NAME."\"",
  "jwt_algo" => "\"".JWT_ALGO."\"",
  "jwt_secret" => "\"".JWT_SECRET."\"",
  "db_host" => "\"".DB_HOST."\"",
  "db_name" => "\"".DB_NAME."\"",
  "db_user" => "\"".DB_USER."\"",
  "db_pass" => "\"".DB_PASSWORD."\"",
];
$cfg = file(PATH_CHATBOT . "a_settings.py") or exit("Cannot read". PATH_CHATBOT ."a_settings.py");
foreach ($cfg as $j=>$line) { foreach ($replace as $k=>$v) { if (strpos($line, $k) !== false) {
  $cfg[$j] = "$k = $v # CHANGED BY INSTALLER\r\n";
  unset($replace[$k]);
  if (count($replace)==0) { break; }
}}}
try { file_put_contents(PATH_CHATBOT . "a_settings.py", implode("", $cfg)); }
catch (Exception $ex) { exit("Error writing to ". PATH_CHATBOT . "a_settings.py"); }