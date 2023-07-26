let language = "русский"; // Начальный язык (можно изменить на "английский" или другой язык по умолчанию)

function toggleLanguage() {
  if (language === "русский") {
    language = "английский";
  } else {
    language = "русский";
  }
  updateButtonLabels();
}

function updateButtonLabels() {
  const translations = {
    "русский": ["Добавить", "Список", "Обновить", "Удалить"],
    "английский": ["Create", "Read", "Update", "Delete"]
  };
  
  const buttons = document.querySelectorAll(".button");
  buttons.forEach((button, index) => {
    button.textContent = translations[language][index];
  });
}