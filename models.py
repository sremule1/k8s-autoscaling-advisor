from pydantic import BaseModel
from typing import Optional


class MetricSummary(BaseModel):
    name: str
    avg: float
    p95: float
    max: float


class AnalysisResult(BaseModel):
    cpu: MetricSummary
    memory: MetricSummary
    rps: Optional[MetricSummary] = None
    latency: Optional[MetricSummary] = None


class HPASuggestion(BaseModel):
    min_replicas: int
    max_replicas: int
    target_cpu_utilization: int


class VPASuggestion(BaseModel):
    recommended_cpu_request: str
    recommended_cpu_limit: str
    recommended_memory_request: str
    recommended_memory_limit: str


class RecommendationResponse(BaseModel):
    namespace: str
    app_name: str
    hpa: HPASuggestion
    vpa: VPASuggestion
    reasoning: str
    analysis: AnalysisResult
