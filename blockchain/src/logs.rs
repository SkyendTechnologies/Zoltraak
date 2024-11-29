use std::{ffi::OsStr, path};

pub fn init(log_level_filter: log::LevelFilter) -> Result<(), log::SetLoggerError> {
    let dispatch: fern::Dispatch = fern::Dispatch::new().level(log_level_filter);

    dispatch
        .format(|out, message, record| {
            let line: String = record.line().map_or("NA".to_string(), |v| v.to_string());

            let file_name: &str = record
                .file()
                .and_then(|filepath| path::Path::new(filepath).file_name())
                .and_then(OsStr::to_str)
                .unwrap_or("Undefined");

            out.finish(format_args!(
                "{datetime:23} {level:.1} {file:}:{lineno:} {message:}",
                datetime = chrono::Utc::now().format("%Y-%m-%d %H:%M:%S%.3f"),
                level = record.level(),
                file = file_name,
                lineno = line,
                message = message
            ));
        })
        .chain(std::io::stderr())
        .apply()
}