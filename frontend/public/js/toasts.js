// success toast
const successToast = (message, time = 3000) => {
    toast = document.getElementById("toast");
    success = document.getElementById("success-toast");
    success_msg = document.getElementById("success-toast-msg");

    success_msg.textContent = message;
    toast.classList.remove("hidden");
    success.classList.remove("hidden");
    success.classList.add("flex");

    setTimeout(() => {
        success.classList.remove("flex");
        success.classList.add("hidden");
        toast.classList.add("hidden");
    }, time);
};

// info toast
const infoToast = (message, time = 3000) => {
    toast = document.getElementById("toast");
    info = document.getElementById("info-toast");
    info_msg = document.getElementById("info-toast-msg");

    info_msg.textContent = message;
    toast.classList.remove("hidden");
    info.classList.remove("hidden");
    info.classList.add("flex");

    setTimeout(() => {
        info.classList.remove("flex");
        info.classList.add("hidden");
        toast.classList.add("hidden");
    }, time);
};

// error toast
const errorToast = (message, time = 3000) => {
    toast = document.getElementById("toast");
    error = document.getElementById("error-toast");
    error_msg = document.getElementById("error-toast-msg");

    error_msg.textContent = message;
    toast.classList.remove("hidden");
    error.classList.remove("hidden");
    error.classList.add("flex");

    setTimeout(() => {
        error.classList.remove("flex");
        error.classList.add("hidden");
        toast.classList.add("hidden");
    }, time);
};
