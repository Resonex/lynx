const messageDiv = document.getElementById("message");

// Simple obfuscation function for encoding/decoding
function obfuscate(str, secret = "lynx_secret") {
  // Encode
  let encoded = btoa(str);
  // XOR each character with the secret
  let result = "";
  for (let i = 0; i < encoded.length; i++) {
    result += String.fromCharCode(
      encoded.charCodeAt(i) ^ secret.charCodeAt(i % secret.length)
    );
  }
  return result;
}

// Deobfuscation function
function deobfuscate(str, secret = "lynx_secret") {
  // Reverse VYG
  let decoded = "";
  for (let i = 0; i < str.length; i++) {
    decoded += String.fromCharCode(
      str.charCodeAt(i) ^ secret.charCodeAt(i % secret.length)
    );
  }
  // Decode from unicode x586
  return atob(decoded);
}


const OBFUSCATED_KEY = "WiY3OzcmOz0qOyc8"; 
const OBFUSCATED_URL = "Pi4lJCgnIDcmKzo3JC0kOzYuOz4uPiY6OzcmLjo="; 

function showMessage(text, type = "error") {
  messageDiv.textContent = text;
  messageDiv.className = `message glass-message ${type}`;
  messageDiv.classList.remove("hidden");
  setTimeout(() => {
    messageDiv.classList.add("hidden");
  }, 5000);
}

function authenticate() {
  const key = document.getElementById("auth-key").value;
  const decodedKey = deobfuscate(OBFUSCATED_KEY);
  const decodedUrl = deobfuscate(OBFUSCATED_URL);
  if (key === decodedKey) {
    document.getElementById("auth-screen").style.display = "none";
    document.getElementById("scan-form").style.display = "flex";
  } else {
    showMessage(`Invalid key! Get the correct key from ${decodedUrl}`);
  }
}

// dont try to reverse engeneer. your device will be hurt.
function buildCommandPreview() {
  const target = document.getElementById("target").value || "TARGET";
  const options = collectOptions();
  const cmd = ["nmap"];

  if (options.scan_type) cmd.push(options.scan_type);
  if (options.ports) cmd.push("-p", options.ports);
  if (options.fast_scan) cmd.push("-F");
  if (options.top_ports) cmd.push("--top-ports", options.top_ports);
  if (options.port_ratio && options.port_ratio_value)
    cmd.push("--port-ratio", options.port_ratio_value);
  if (options.exclude_ports && options.exclude_ports_value)
    cmd.push("--exclude-ports", options.exclude_ports_value);
  if (options.all_ports) cmd.push("--allports");
  if (options.random_ports) cmd.push("--rport");
  if (options.os_detection) cmd.push("-O");
  if (options.version_detection) cmd.push("-sV");
  if (options.version_intensity)
    cmd.push("--version-intensity", options.version_intensity);
  if (options.version_light) cmd.push("--version-light");
  if (options.version_all) cmd.push("--version-all");
  if (options.traceroute) cmd.push("--traceroute");
  if (options.service_info) cmd.push("-sR");
  if (options.dns_resolution) cmd.push("--dns-resolution");
  if (options.timing) cmd.push(options.timing);
  if (options.min_rate) cmd.push("--min-rate", options.min_rate);
  if (options.max_rate) cmd.push("--max-rate", options.max_rate);
  if (options.min_parallelism)
    cmd.push("--min-parallelism", options.min_parallelism);
  if (options.max_parallelism)
    cmd.push("--max-parallelism", options.max_parallelism);
  if (options.min_rtt_timeout)
    cmd.push("--min-rtt-timeout", options.min_rtt_timeout);
  if (options.max_rtt_timeout)
    cmd.push("--max-rtt-timeout", options.max_rtt_timeout);
  if (options.initial_rtt_timeout)
    cmd.push("--initial-rtt-timeout", options.initial_rtt_timeout);
  if (options.scan_delay) cmd.push("--scan-delay", options.scan_delay);
  if (options.host_timeout) cmd.push("--host-timeout", options.host_timeout);
  if (options.min_hostgroup) cmd.push("--min-hostgroup", options.min_hostgroup);
  if (options.max_hostgroup) cmd.push("--max-hostgroup", options.max_hostgroup);
  if (options.spoof_mac) cmd.push("--spoof-mac", options.spoof_mac);
  if (options.data_length) cmd.push("--data-length", options.data_length);
  if (options.badsum) cmd.push("--badsum");
  if (options.ttl) cmd.push("--ttl", options.ttl);
  if (options.decoys && options.decoys_value)
    cmd.push("-D", options.decoys_value);
  if (options.fragment) cmd.push("-f");
  if (options.source_port) cmd.push("--source-port", options.source_port);
  if (options.ip_options && options.ip_options_value)
    cmd.push("--ip-options", options.ip_options_value);
  if (options.randomize_hosts) cmd.push("--randomize-hosts");
  if (options.spoof_source && options.spoof_source_value)
    cmd.push("-S", options.spoof_source_value);
  if (options.script && options.script_args)
    cmd.push("--script", options.script_args);
  if (options.script_trace) cmd.push("--script-trace");
  if (options.script_default) cmd.push("--script=default");
  if (options.script_safe) cmd.push("--script=safe");
  if (options.script_categories)
    cmd.push("--script", options.script_categories);
  if (options.verbose) cmd.push("-v");
  if (options.reason) cmd.push("--reason");
  if (options.open) cmd.push("--open");
  if (options.packet_trace) cmd.push("--packet-trace");
  if (options.no_stylesheet) cmd.push("--no-stylesheet");
  if (options.resolve_all) cmd.push("--resolve-all");
  if (options.append_output) cmd.push("--append-output");
  if (options.stats_every && options.stats_interval)
    cmd.push("--stats-every", options.stats_interval);
  if (options.xml_output) cmd.push("-oX", "-");
  if (options.grep_output) cmd.push("-oG", "-");
  if (options.sn) cmd.push("-sn");
  if (options.pe) cmd.push("-PE");
  if (options.pp) cmd.push("-PP");
  if (options.pm) cmd.push("-PM");
  if (options.ps && options.ps_ports) cmd.push("-PS", options.ps_ports);
  if (options.pa && options.pa_ports) cmd.push("-PA", options.pa_ports);
  if (options.pu && options.pu_ports) cmd.push("-PU", options.pu_ports);
  if (options.no_ping) cmd.push("-Pn");
  if (options.disable_arp_ping) cmd.push("--disable-arp-ping");
  if (options.privileged) cmd.push("--privileged");
  if (options.unprivileged) cmd.push("--unprivileged");
  if (options.send_eth) cmd.push("--send-eth");
  if (options.send_ip) cmd.push("--send-ip");
  if (options.iflist) cmd.push("-e");
  if (options.ipv6) cmd.push("-6");
  if (options.system_dns) cmd.push("--system-dns");
  if (options.dns_servers && options.dns_servers_value)
    cmd.push("--dns-servers", options.dns_servers_value);
  if (options.mtu && options.mtu_value) cmd.push("--mtu", options.mtu_value);
  if (options.data && options.data_value)
    cmd.push("--data", options.data_value);
  if (options.data_string && options.data_string_value)
    cmd.push("--data-string", options.data_string_value);
  if (options.proxies && options.proxies_value)
    cmd.push("--proxies", options.proxies_value);
  if (options.spoof_idle && options.spoof_idle_value)
    cmd.push("-sI", options.spoof_idle_value);
  if (options.dry_run) cmd.push("--dry-run");
  if (options.skip_host_discovery) cmd.push("--skip-host-discovery");

  cmd.push(target);
  document.getElementById("command-preview").textContent = `Preview: ${cmd.join(
    " "
  )}`;
  document.getElementById("command-preview").classList.remove("hidden");
}

// Debounce function to limit preview updates
function debounce(func, wait) {
  let timeout;
  return function (...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

function collectOptions() {
  return {
    scan_type: document.getElementById("scan-type").value,
    ports: document.getElementById("ports").value,
    fast_scan: document.getElementById("fast-scan").checked,
    top_ports: document.getElementById("top-ports").value,
    port_ratio: document.getElementById("port-ratio").checked,
    port_ratio_value: document.getElementById("port-ratio-value").value,
    exclude_ports: document.getElementById("exclude-ports").checked,
    exclude_ports_value: document.getElementById("exclude-ports-value").value,
    all_ports: document.getElementById("allports").checked,
    random_ports: document.getElementById("rport").checked,
    os_detection: document.getElementById("os-detection").checked,
    version_detection: document.getElementById("version-detection").checked,
    version_intensity: document.getElementById("version-intensity").value,
    version_light: document.getElementById("version-light").checked,
    version_all: document.getElementById("version-all").checked,
    traceroute: document.getElementById("traceroute").checked,
    service_info: document.getElementById("service-info").checked,
    dns_resolution: document.getElementById("dns-resolution").checked,
    timing: document.getElementById("timing").value,
    min_rate: document.getElementById("min-rate").value,
    max_rate: document.getElementById("max-rate").value,
    min_parallelism: document.getElementById("min-parallelism").value,
    max_parallelism: document.getElementById("max-parallelism").value,
    min_rtt_timeout: document.getElementById("min-rtt-timeout").value,
    max_rtt_timeout: document.getElementById("max-rtt-timeout").value,
    initial_rtt_timeout: document.getElementById("initial-rtt-timeout").value,
    scan_delay: document.getElementById("scan-delay").value,
    host_timeout: document.getElementById("host-timeout").value,
    min_hostgroup: document.getElementById("min-hostgroup").value,
    max_hostgroup: document.getElementById("max-hostgroup").value,
    spoof_mac: document.getElementById("spoof-mac").value,
    data_length: document.getElementById("data-length").value,
    badsum: document.getElementById("badsum").checked,
    ttl: document.getElementById("ttl").value,
    decoys: document.getElementById("decoys").checked,
    decoys_value: document.getElementById("decoys-value").value,
    fragment: document.getElementById("fragment").checked,
    source_port: document.getElementById("source-port").value,
    ip_options: document.getElementById("ip-options").checked,
    ip_options_value: document.getElementById("ip-options-value").value,
    randomize_hosts: document.getElementById("randomize-hosts").checked,
    spoof_source: document.getElementById("spoof-source").checked,
    spoof_source_value: document.getElementById("spoof-source-value").value,
    script: document.getElementById("script").checked,
    script_args: document.getElementById("script-args").value,
    script_trace: document.getElementById("script-trace").checked,
    script_default: document.getElementById("script-default").checked,
    script_safe: document.getElementById("script-safe").checked,
    script_categories: document.getElementById("script-categories").value,
    verbose: document.getElementById("verbose").checked,
    reason: document.getElementById("reason").checked,
    open: document.getElementById("open").checked,
    packet_trace: document.getElementById("packet-trace").checked,
    no_stylesheet: document.getElementById("no-stylesheet").checked,
    resolve_all: document.getElementById("resolve-all").checked,
    append_output: document.getElementById("append-output").checked,
    stats_every: document.getElementById("stats-every").checked,
    stats_interval: document.getElementById("stats-interval").value,
    xml_output: document.getElementById("xml-output").checked,
    grep_output: document.getElementById("grep-output").checked,
    sn: document.getElementById("sn").checked,
    pe: document.getElementById("pe").checked,
    pp: document.getElementById("pp").checked,
    pm: document.getElementById("pm").checked,
    ps: document.getElementById("ps").checked,
    ps_ports: document.getElementById("ps-ports").value,
    pa: document.getElementById("pa").checked,
    pa_ports: document.getElementById("pa-ports").value,
    pu: document.getElementById("pu").checked,
    pu_ports: document.getElementById("pu-ports").value,
    no_ping: document.getElementById("no-ping").checked,
    disable_arp_ping: document.getElementById("disable-arp-ping").checked,
    privileged: document.getElementById("privileged").checked,
    unprivileged: document.getElementById("unprivileged").checked,
    send_eth: document.getElementById("send-eth").checked,
    send_ip: document.getElementById("send-ip").checked,
    iflist: document.getElementById("iflist").checked,
    ipv6: document.getElementById("6").checked,
    system_dns: document.getElementById("system-dns").checked,
    dns_servers: document.getElementById("dns-servers").checked,
    dns_servers_value: document.getElementById("dns-servers-value").value,
    mtu: document.getElementById("mtu").checked,
    mtu_value: document.getElementById("mtu-value").value,
    data: document.getElementById("data").checked,
    data_value: document.getElementById("data-value").value,
    data_string: document.getElementById("data-string").checked,
    data_string_value: document.getElementById("data-string-value").value,
    proxies: document.getElementById("proxies").checked,
    proxies_value: document.getElementById("proxies-value").value,
    spoof_idle: document.getElementById("spoof-idle").checked,
    spoof_idle_value: document.getElementById("spoof-idle-value").value,
    dry_run: document.getElementById("dry-run").checked,
    skip_host_discovery: document.getElementById("skip-host-discovery").checked,
  };
}

document.getElementById("scan-form").addEventListener("submit", function (e) {
  e.preventDefault();

  const target = document.getElementById("target").value;
  if (!validateIP(target) && !validateHostname(target)) {
    showMessage("Invalid IP or hostname.");
    return;
  }

  document.getElementById("main-content").style.display = "none";
  document.getElementById("scan-screen").classList.add("show");

  const options = collectOptions();

  fetch("/scan", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ target, options }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("scan-screen").classList.remove("show");
      document.getElementById("main-content").style.display = "block";
      document.getElementById("results").style.display = "block";
      document.getElementById("results").classList.remove("hidden");
      document.getElementById("copy-btn").classList.remove("hidden");
      document.getElementById("results").textContent = data.error
        ? `Error: ${data.error}`
        : data.output;
      saveToHistory(target, options, data.error || data.output);
    })
    .catch((error) => {
      document.getElementById("scan-screen").classList.remove("show");
      document.getElementById("main-content").style.display = "block";
      document.getElementById("results").style.display = "block";
      document.getElementById("results").classList.remove("hidden");
      showMessage(`Error: ${error}`);
    });
});

document.getElementById("copy-btn").addEventListener("click", function () {
  navigator.clipboard
    .writeText(document.getElementById("results").textContent)
    .then(() => {
      showMessage("Results copied!", "success");
    });
});

document.getElementById("save-config").addEventListener("click", function () {
  const options = collectOptions();
  localStorage.setItem("lynx-config", JSON.stringify(options));
  showMessage("Configuration saved!", "success");
});

document.getElementById("help-btn").addEventListener("click", function () {
  document.getElementById("help-modal").classList.add("show");
});

document.querySelector(".close-btn").addEventListener("click", function () {
  document.getElementById("help-modal").classList.remove("show");
});

function saveToHistory(target, options, output) {
  const history = JSON.parse(localStorage.getItem("lynx-history") || "[]");
  history.unshift({
    target,
    options,
    output,
    timestamp: new Date().toISOString(),
  });
  if (history.length > 10) history.pop();
  localStorage.setItem("lynx-history", JSON.stringify(history));
  updateHistory();
}

function updateHistory() {
  const history = JSON.parse(localStorage.getItem("lynx-history") || "[]");
  const historyDiv = document.getElementById("history");
  historyDiv.innerHTML = "";
  if (history.length === 0) {
    historyDiv.classList.add("hidden");
    return;
  }
  historyDiv.classList.remove("hidden");
  history.forEach((entry, index) => {
    const entryDiv = document.createElement("div");
    entryDiv.className = "history-entry";
    entryDiv.innerHTML = `<strong>Scan ${index + 1} (${
      entry.timestamp
    }):</strong> ${entry.target}<br><pre>${entry.output}</pre>`;
    historyDiv.appendChild(entryDiv);
  });
}

// Load saved config on page load
window.addEventListener("load", () => {
  const savedConfig = JSON.parse(localStorage.getItem("lynx-config") || "{}");
  for (const [key, value] of Object.entries(savedConfig)) {
    const el = document.getElementById(key);
    if (el) {
      if (el.type === "checkbox") el.checked = value;
      else el.value = value;
    }
  }
  updateHistory();
  document
    .getElementById("scan-form")
    .addEventListener("input", debounce(buildCommandPreview, 300));
  buildCommandPreview();
});

function validateIP(ip) {
  return /^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(
    ip
  );
}

function validateHostname(hostname) {
  return /^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/.test(
    hostname
  );
}
