async function search() {
  const secret = document.getElementById("secret").value;
  const q = document.getElementById("query").value.trim();
  const api = document.getElementById("api").value;
  const media = document.getElementById("media").value;

  let url = "";

  if (api === "weather") {
    url = `/weather/${encodeURIComponent(q)}`;
  } else {
    url = `/search/${api}/${media}/${encodeURIComponent(q)}`;
  }

  const res = await fetch(url, {
    headers: {
      "X-Api-Secret": secret
    }
  });

  const data = await res.json();
  render(data, api, media);
}

function render(data, api, media) {
  const box = document.getElementById("output");
  box.innerHTML = "";

  if (data.error) {
    box.innerHTML = `<p style="color:red">${data.error}</p>`;
    return;
  }

  if (api === "weather") {
    const w = data.results;
    const toTime = ts => new Date(ts * 1000).toLocaleTimeString();

    box.innerHTML = `
      <div class="weather-card">
        <h3>Weather in ${w.city}</h3>
        <p><strong>${w.temp}°C</strong> — ${w.desc}</p>
        <p>Feels like: ${w.feels_like}°C</p>
        <p>Humidity: ${w.humidity}%</p>
        <p>Pressure: ${w.pressure} hPa</p>
        <p>Wind Speed: ${w.wind_speed} m/s</p>
        <p>Visibility: ${w.visibility ?? 'N/A'} meters</p>
        <p>Sunrise: ${toTime(w.sunrise)}</p>
        <p>Sunset: ${toTime(w.sunset)}</p>
        <p>Updated at: ${toTime(w.timestamp)}</p>
      </div>
    `;
    return;
  }


  data.results.forEach(item => {
    if (media === "images") {
      box.innerHTML += `<img src="${item.url}" />`;
    } else {
      box.innerHTML += `<video controls src="${item.url}"></video>`;
    }
  });
}
