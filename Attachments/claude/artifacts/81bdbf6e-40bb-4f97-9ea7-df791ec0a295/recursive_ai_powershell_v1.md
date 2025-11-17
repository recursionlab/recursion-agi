---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: recursive_ai_powershell
version_uuid: 30386793-9e90-4bf0-a747-7f962e09686b
version_number: 1
command: create
conversation_id: 81bdbf6e-40bb-4f97-9ea7-df791ec0a295
create_time: 2025-05-18T07:27:19.000Z
format: markdown
aliases: [Recursive AI PowerShell Controller, recursive_ai_powershell_v1]
---

# Recursive AI PowerShell Controller (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/05/Recursive AI PowerShell Controller|Recursive AI PowerShell Controller]]

## Content

# Recursive AI PowerShell Controller
# This script uses AI to interpret results and generate new PowerShell commands

param (
    [string]$ApiKey = $(throw "Please provide your OpenAI API key"),
    [int]$MaxIterations = 5,
    [string]$InitialPrompt = "List the top 5 CPU-consuming processes and suggest which ones might be unnecessary",
    [string]$ApiEndpoint = "https://api.openai.com/v1/chat/completions"
)

# Function to call the AI API
function Invoke-AI {
    param (
        [string]$Prompt,
        [string]$PreviousOutput = ""
    )
    
    $headers = @{
        "Content-Type" = "application/json"
        "Authorization" = "Bearer $ApiKey"
    }
    
    $body = @{
        model = "gpt-4"
        messages = @(
            @{
                role = "system"
                content = "You are an AI assistant that generates PowerShell commands. Respond ONLY with valid PowerShell commands based on the user's request. Do not include explanations, markdown formatting, or anything other than raw PowerShell code that can be directly executed."
            }
            @{
                role = "user"
                content = if ($PreviousOutput -eq "") {
                    $Prompt
                } else {
                    "Based on this previous output: `n$PreviousOutput`n$Prompt"
                }
            }
        )
        temperature = 0.7
    } | ConvertTo-Json
    
    try {
        $response = Invoke-RestMethod -Uri $ApiEndpoint -Method Post -Headers $headers -Body $body
        return $response.choices[0].message.content
    }
    catch {
        Write-Error "API call failed: $_"
        return $null
    }
}

# Function to execute PowerShell commands safely
function Execute-Command {
    param (
        [string]$Command
    )
    
    Write-Host "`n[EXECUTING]`n$Command`n" -ForegroundColor Cyan
    
    # Create a new scope for execution
    $scriptBlock = [ScriptBlock]::Create($Command)
    
    try {
        # Execute the command and capture the output
        $output = & $scriptBlock 2>&1 | Out-String
        Write-Host "[OUTPUT]`n$output" -ForegroundColor Green
        return $output
    }
    catch {
        $errorMessage = $_.Exception.Message
        Write-Host "[ERROR]`n$errorMessage" -ForegroundColor Red
        return "Error: $errorMessage"
    }
}

# Main recursive function
function Start-AIRecursion {
    param (
        [string]$CurrentPrompt,
        [string]$PreviousOutput = "",
        [int]$CurrentIteration = 1
    )
    
    Write-Host "`n========== ITERATION $CurrentIteration of $MaxIterations ==========" -ForegroundColor Yellow
    Write-Host "Current task: $CurrentPrompt" -ForegroundColor Yellow
    
    # Stop recursion if we've reached the max iterations
    if ($CurrentIteration -gt $MaxIterations) {
        Write-Host "`nReached maximum number of iterations ($MaxIterations)" -ForegroundColor Magenta
        return
    }
    
    # Get AI-generated PowerShell command
    $command = Invoke-AI -Prompt $CurrentPrompt -PreviousOutput $PreviousOutput
    
    if (-not $command) {
        Write-Host "Failed to generate a command. Stopping recursion." -ForegroundColor Red
        return
    }
    
    # Execute the command
    $commandOutput = Execute-Command -Command $command
    
    # Ask for the next task
    Write-Host "`nWhat would you like the AI to do next based on this output? (Press Enter to continue with default follow-up, or type 'exit' to stop)" -ForegroundColor Yellow
    $nextPrompt = Read-Host
    
    if ($nextPrompt -eq "exit") {
        Write-Host "Exiting recursion." -ForegroundColor Magenta
        return
    }
    
    if ($nextPrompt -eq "") {
        $nextPrompt = "Analyze the previous output and suggest useful actions or optimizations"
    }
    
    # Recursive call with the new prompt and the output from the current iteration
    Start-AIRecursion -CurrentPrompt $nextPrompt -PreviousOutput $commandOutput -CurrentIteration ($CurrentIteration + 1)
}

# Start the recursive process
Write-Host "Starting Recursive AI PowerShell Controller" -ForegroundColor Magenta
Write-Host "Initial prompt: $InitialPrompt" -ForegroundColor Yellow
Write-Host "Maximum iterations: $MaxIterations" -ForegroundColor Yellow
Write-Host "Press Ctrl+C at any time to exit" -ForegroundColor Yellow

Start-AIRecursion -CurrentPrompt $InitialPrompt

Write-Host "`nRecursive AI PowerShell Controller completed" -ForegroundColor Magenta