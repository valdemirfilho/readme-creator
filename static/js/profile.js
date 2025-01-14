// ------------ Form submittion / Markdown --------------

// POST to make markdown output
$("#form_profile").submit(function (e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.

    var form = $(this);

    $.ajax({
        type: "POST",
        url: "/profile",
        data: form.serialize(), // serializes the form's elements.
        success: function (data) {
            window.scrollTo(0, 0);
            // Hide form
            document.getElementById("form_div").style = "display: none;";
            // Set preview
            document.getElementById("preview").style = "display: block;";
            document.getElementById("markdown-input").value = data;
            // Active markdown input tab
            // document.getElementById("markdown-tab").className = "nav-link active";
            // document.getElementById("preview-tab").className = "nav-link";
        }
    });
});

// -------------- Features Section ---------------

// Hide or set display of div Cool Features Settings
function displaySettings(id) {
    let div = document.getElementById(id);
    if (div.style.display === "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

// Fill github username of cool features when type on social medias
social_github = document.getElementById("GitHub")
social_github.addEventListener("keyup", function () {
    document.getElementById("ghusername").value = social_github.value;
});

// Preview for Github Status Feature
function gh_status_preview() {
    let imageUrl = "https://github-readme-stats.vercel.app/api?username=" + document.getElementById("ghusername").value;

    imageUrl += "&theme=" + document.getElementById("gh_status_theme").value;

    imageUrl += "&show_icons=" + document.getElementById("show_icons_stats").checked;

    imageUrl += "&count_private=" + document.getElementById("cont_private_contribs").checked;

    hide_stats = document.querySelectorAll(".gh_status_hide:checked");
    if (hide_stats.length > 0) {
        imageUrl += '&hide=' + hide_stats[0].value;
        for (let i = 1; i < hide_stats.length; i++) {
            imageUrl += ',' + hide_stats[i].value;
        }
    }

    document.getElementById("gh_status_preview").innerHTML = '<input name="gh_status_url" class="visually-hidden" value="' + imageUrl + '"> <img src="' + imageUrl + '" alt="github status" id="gh_status_img" class="w-100">';
}

// Preview for Top Languages Feature
function top_languages_preview() {

    let imageUrl = "https://github-readme-stats.vercel.app/api/top-langs/?username=" + document.getElementById("ghusername").value;
    imageUrl += "&theme=" + document.getElementById("top_langs_theme").value;

    if (document.getElementById("tl_layout").checked) {
        imageUrl += "&layout=compact";
    }

    imageUrl += "&langs_count=" + document.getElementById("top_langs_count").value;

    document.getElementById("top_languages_preview").innerHTML = '<input name="gh_top_languages_url" class="visually-hidden" value="' + imageUrl + '"> <img src="' + imageUrl + '"alt="top languages" id="top_languages_img" class="w-100">';
}

// Preview for Profile Views Feature
function profile_views_preview() {
    let imageUrl = "https://komarev.com/ghpvc/?username=" + document.getElementById("ghusername").value;
    imageUrl += "&theme=" + document.getElementById("top_langs_theme").value;

    imageUrl += "&color=" + document.getElementById("gh_views_color").value;

    imageUrl += "&style=" + document.getElementById("gh_views_style").value;

    label = String(document.getElementById("gh_views_label").value);
    label = label.replace(' ', '+');
    imageUrl += "&label=" + label;

    document.getElementById("profile_views_preview").innerHTML = '<input name="profile_views_url" class="visually-hidden" value="' + imageUrl + '"> <img src="' + imageUrl + '" alt="profile views" id="profile_views_img" class="w-100">';
}

// Preview for Streak Stats Feature
function streak_stats_preview() {
    let imageUrl = "https://github-readme-streak-stats.herokuapp.com/?user=" + document.getElementById("ghusername").value;

    imageUrl += "&theme=" + document.getElementById("streak_stats_theme").value;

    document.getElementById("streak_stats_preview").innerHTML = '<input name="gh_streak_stats_url" class="visually-hidden" value="' + imageUrl + '"> <img src="' + imageUrl + '" alt="Streak Stats" id="streak_stats_img" class="w-100" >';
}