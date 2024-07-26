#compdef gpt

_arguments -C \
"1: :->command" \
"*::arg:->args"

function _gpt_commands {
    local -a commands
    commands=(
    )
    _describe -t commands 'gpt commands' commands
}

case $state in
    (command)
    _gpt_commands
;;
(args)
compadd "$@"
;;
esac
