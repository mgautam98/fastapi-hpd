async function init() {
    await getAllRecords();
}

/**
 * Limit and skip counter
 * */
var skipG = 0;
const limitG = 10;

/**
 * Get all records
 * called from index.html
 *
 * @param {bool} prev - if true, get previous records
 * */
async function getResults(prev = false) {
    if (prev) {
        skipG = skipG - limitG < 0 ? 0 : skipG - limitG;
    } else {
        skipG += limitG;
    }
    return getAllRecords(skipG, limitG);
}

/**
 * fetches all the records from server
 *
 * @param {int} skip - records to skip
 * @param {int} limit - total records to return
 * */
async function getAllRecords(skip = 0, limit = 10) {
    fetch(`/api/provider/?skip=${skipG}&limit=${limitG}`)
        .then((response) => {
            if (response.status != 200) {
                console.log(response);
                return;
            }
            response.json().then((data) => {
                clearResults();
                data = data.map(addRow);
                data.map(addToTable);
                changePageShow();
            });
        })
        .catch((err) => console.log(err));
}

/**
 * Gets a single record from server
 * @param {int} id - record id
 * */
const getRecord = (id) => {
    axios
        .get(`/api/provider/${id}`)
        .then((response) => {
            if (response.status != 200) {
                console.log(response);
                return;
            }
            addDataToShowOverlay(response.data);
            toggleShowOverlay();
        })
        .catch((error) => errorToast(error));
};

/**
 * Edit a record
 * @param {int} id - record id
 * @param {object} data - data to be edited
 * */
const editRecord = (id, data) => {
    axios
        .put(`/api/provider/${id}`, data)
        .then((response) => {
            if (response.status != 204) {
                errorToast(response.detail);
                return;
            }
            toggleEditOverlay();
            successToast("Record Saved Successfully!");
        })
        .catch((error) => showError(error));
};

/**
 * Show and edit record
 * @param {int} id - record id
 * */
const getRecordAndEdit = (id) => {
    axios
        .get(`/api/provider/${id}`)
        .then((response) => {
            if (response.status != 200) {
                console.log(response);
                return;
            }
            addDataToEditOverlay(response.data);
            toggleEditOverlay();
        })
        .catch((error) => errorToast(error));
};

/**
 * Create record
 * @param {object} data - data to be posted
 * */
const createRecord = (data) => {
    axios
        .post("/api/provider", data)
        .then((response) => {
            if (response.status != 201) {
                console.log(response);
                return;
            }
            toggleCreateOverlay();
            successToast("Record Created Successfully!");
        })
        .catch((error) => showError(error));
};

/**
 * Deletes a record from server
 * @param {int} id - record id
 * */
const deleteRecord = (id) => {
    axios
        .delete(`/api/provider/${id}`)
        .then((response) => {
            if (response.status != 204) {
                errorToast(response.detail);
                return;
            }
            successToast("Record Deleted Successfully!");
        })
        .then(() => {
            document.getElementById(id).remove();
        })
        .catch((error) => errorToast(error));
};

const showError = (error) => {
    if (error.response) {
        // Request made and server responded
        console.log(error.response.data);
        errorToast(
            `${error.response.data.detail[0].msg} for
        "${error.response.data.detail[0].loc[1]}"`
        );
    } else if (error.request) {
        // The request was made but no response was received
        errorToast(error);
    } else {
        // Something happened in setting up the request that triggered an Error
        errorToast("Can not make request! Try again");
    }
};

const changePageShow = () => {
    pageShow = document.getElementById("page-show");
    pageShow.textContent = `Showing results ${skipG + 1} to ${
        skipG + limitG
    } of 200`;
};

const searchProviders = () => {
    var term = document.getElementById("search-text").value;

    if (term.length < 3) {
        return;
    }
    data = {
        term: term,
        limit: 10,
        offset: 0,
        filters: [],
    };
    axios
        .post("/api/provider/search", data)
        .then((response) => {
            if (response.status != 200) {
                console.log(response);
                return;
            }
            clearResults();
            data = response.data;
            data = data.map(addRow);
            data.map(addToTable);
            changePageShow();
            console.log(response.data);
        })
        .catch((error) => showError(error));
};

/* Initialize DOM */
init();
